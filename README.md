# BambuAppDaemon

_App to update images on the Panda Touch when starting a print on the Bambu._

## Installation

Download the `bambu` directory from inside the `apps` directory here to your local `apps` directory, then add the configuration to enable the `bambu` module.

You need to have the [ha-bambulab](https://github.com/greghesp/ha-bambulab) integration working on your home assistant for it to work.

## App configuration

```yaml
bambu:
  module: bambu
  class: BambuImage
  image_entity: "image.bambu_p1s_cover_image"
  ha_url: "http://home.local:8123"
  panda_ip: "192.168.86.88"
```

key | optional | type | default | description
-- | -- | -- | -- | --
`module` | False | string | | The module name of the app.
`class` | False | string | | The name of the Class.
`image_entity` | False | string | | The entity id of the image provided by the https://github.com/greghesp/ha-bambulab integration.
`ha_url` | False | string | | The root URL for your home assistant.
`panda_ip` | False | string | | The IP address of your Panda Touch.
