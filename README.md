# Bambu Image Updater AppDaemon

_App to update images on the Panda Touch when starting a print on the Bambu._

  ## Install using HACS

  To install this AppDaemon app using HACS, follow these steps:

  1. **Access HACS**: 
     - Click on the "HACS" option in the sidebar.
     - Click on "Automation"

  2. **Add a Custom Repository**:
     - Click on the three dots in the top right corner and select "Custom repositories".
     - Enter this URL: `https://github.com/gpambrozio/BambuAppDaemon.git`
     - Select "AppDaemon" as the category.
     - Click "Add".

  4. **Install the App**:
     - Click on the "Explore & Download Repositories" section.
     - Search for "Bambu".
     - Click on the app and then click "Install".

  5. ** Add the Pillow library to AppDaemon **
     - See instructions below.

  6. **Configure the App**:
     - After installation, go to the AppDaemon configuration directory.
     - Edit the `apps.yaml` file to configure the app according to your needs.

## Manual Installation

Download the `BambuAppDaemon` directory from inside the `apps` directory here to your local `apps` directory, then edit `apps.yaml` to enable the `BambuAppDaemon` module.

You need to have the [ha-bambulab](https://github.com/greghesp/ha-bambulab) integration working on your home assistant for it to work.

You also need to add the Pillow library to AppDaemon (see below)

## Add the Pillow library to AppDaemon

* On Home assistant, go to Settings
* Open Add-Ons
* Click on AppDaemon
* Open the Configuration tab
* In "Python Packages", type "Pillow" (no quotes) and click enter.
* Click on the "Save" button.
* When asked, restart AppDaemon.

## App configuration

```yaml
bambu:
  module: BambuAppDaemon
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
