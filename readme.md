[![CircleCI](https://circleci.com/gh/hafffe/home.svg?style=svg)](https://circleci.com/gh/hafffe/home)

## Home configuration
> A bunch of tools to automate my home

My config to for home-assistant.

### Includes
- [Home-assistant](http://github.com/home-assistant/home-assistant)
- [Docker](https://www.docker.com)
- [Portainer](https://github.com/portainer/portainer)
- [Mosquitto](https://github.com/eclipse/mosquitto)
- [Traefik](https://github.com/containous/traefik)


### Devices
- [Aoetec Z-Stick Gen5](https://aeotec.com/z-wave-usb-stick)
- [Dresden-elektronik Conbee](https://www.dresden-elektronik.de/conbee/)


### Prepare
Before start containers enviroment variables need to be setup in a .env file

```
$ sudo touch .env
$ echo "EMAIL=<redacted>" | sudo tee -a .env
$ echo "DOMAIN=<redacted>" | sudo tee -a .env
```

### Persistent USB
list usb devices with `lsusb`

Get more vendor id for given device

```
$ /bin/udevadm info --name=/dev/ttyUSB0 | grep ID_VENDOR
E: ID_VENDOR_ID=0403
```

Get modell id for given device
```
$ /bin/udevadm info --name=/dev/ttyUSB0 | grep ID_MODEL_ID
E: ID_MODEL_ID=6015
```

Get Serial ID for given device

```
$ /bin/udevadm info --name=/dev/ttyUSB0 | grep SERIAL_SHORT
E: ID_SERIAL_SHORT=ABC01234
```

My usb devices are Aeon [Aeon Z-stick gen 5](https://aeotec.com/z-wave-usb-stick/)
and [Conbee version 1](https://phoscon.de/en/conbee) and have the following attributes.
Check this [this guide](http://hintshop.ludvig.co.nz/show/persistent-names-usb-serial-devices/) to findout details.

Go to `/etc/udev/rules.d` create new file called `99-usb-serial.rules` and add the devices.
Disclaimer: The following paths are just for my usb devices.

zwave:
```
SUBSYSTEM=="tty", ATTRS{idVendor}=="0658", ATTRS{idProduct}=="0200", SYMLINK+="zwave"
```

zigbee:
```
SUBSYSTEM=="tty", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6015", ATTRS{serial}=="DO00KE9N", SYMLINK+="zigbee"
```
