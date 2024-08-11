import appdaemon.plugins.hass.hassapi as hass

import requests
import struct
from io import BytesIO
from PIL import Image

#
# Update Bambu image
#
# Args:
#
# image_entity: The entity id of the image provided by the https://github.com/greghesp/ha-bambulab integration.
# ha_url: The root URL for your home assistant.
# panda_ip: The IP address of your Panda Touch.
#
class BambuImage(hass.Hass):
    max_size = (250, 250)

    def initialize(self):
        self.run_in(self.image_update, 1)
        self.listen_state(self.image_changed, self.args["image_entity"])

    def image_changed(self, entity, attribute, old, new, kwargs):
        self.run_in(self.image_update, 1)

    def image_update(self, cb_args):
        image_url = self.get_entity(self.args["image_entity"]).get_state(attribute="entity_picture")

        if image_url:
            # Fetch the image data
            ha_url = self.args["ha_url"]
            response = requests.get(f"{ha_url}{image_url}")
            if response.status_code != 200:
                self.log(f"Image retrieve failed: {response.status_code}")
                return

            image_data = BytesIO(response.content)
            with Image.open(image_data) as img:
                # Scale the image down to fit within max_size while maintaining aspect ratio
                img.thumbnail(self.max_size)

                # Ensure the image is in RGB mode
                img = img.convert('RGBA')
                width, height = img.size

                # Prepare the binary content
                binary_content = bytearray()

                header = bytes.fromhex('DFAD000001F26E65775F70616E64612E706E67000000')
                binary_content.extend(header)

                # Pack the size as a 4-byte unsigned integer in little endian
                size_bytes = struct.pack('<I', width * height * 3 + 4)
                binary_content.extend(size_bytes)

                dimensions = ((height * 4) << 19) + ((width * 4) << 8) + 5
                dimensions_bytes = struct.pack('<I', dimensions)
                binary_content.extend(dimensions_bytes)

                # Process each pixel row by row
                for y in range(height):
                    for x in range(width):
                        r, g, b, a = img.getpixel((x, y))

                        pixel = (a << 16) + ((r >> 3) << 11) + ((g >> 2) << 5) + (b >>3)
                        pixel_bytes = struct.pack('<I', pixel)[:3]

                        # Append the pixel in BGR format
                        binary_content.extend(pixel_bytes)

                headers = {
                    'Content-Type': 'application/octet-stream;charset=UTF-8',
                }
                panda_ip = self.args["panda_ip"]
                response = requests.post(f"http://{panda_ip}:8080/update_add_file", headers=headers, data=binary_content)
                if response.status_code != 200:
                    self.log(f"Panda Response failed: {response.status_code}")
