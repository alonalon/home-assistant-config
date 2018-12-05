## Home configuration
> A bunch of tools to automate my home

My config to for home-assistant.

### Includes
- [Home-assistant](http://github.com/home-assistant/home-assistant)
- [Docker](https://www.docker.com)
- [Portainer](https://github.com/portainer/portainer)
- [Mosquitto](https://github.com/eclipse/mosquitto)
- [Nginx](https://github.com/nginx/nginx)


### Devices
- [Aoetec Z-Stick Gen5](https://aeotec.com/z-wave-usb-stick)
- [Dresden-elektronik Conbee](https://www.dresden-elektronik.de/conbee/)


### Prepare
Before start containers enviroment variables need to be setup in a .env file
```
$ sudo touch .env
$ echo "DOMAIN_TRAEFIK=<redacted>" | sudo tee -a .env
$ echo "DOMAIN_HOMEASSISTANT=<redacted>" | sudo tee -a .env
$ echo "DOMAIN_DECONZ=<redacted>" | sudo tee -a .env
$ echo "DOMAIN_PORTAINER=<redacted>" | sudo tee -a .env
```