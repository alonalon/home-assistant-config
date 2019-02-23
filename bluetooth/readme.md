# Bluetooth to MQTT presence

*Requirements*
- A MQTT broker to connect to
- Bluetooth enabled hardware
- Bluetooth service disabled on host system

## Installation

1. Copy the source files to your machine
2. Copy the files from the templates folder to your newly created folder. Theese **must** be on the same level as `presence.sh`
3. Add a new container to your docker-compose file, example below.
change the container to fit your preferences.
4. Start your new container with `docker-compose up -d <containername>` (You may need to change permissions on `.sh` files, to let docker be able execute the files)
5. When container is up and running, run `docker exec -it <containername> hcitool scan` to find your devices. It could help to turn bluetooth on/off on your device you try to pair during this process.
6. Put the MAC adress in the `owner_devices` file and run `docker-compose restart <containername>`
6. Check the logs to see if your device is connected with your machine.


### docker-compose example

```
  bluetooth:
    build: ./bluetooth
    image: alonalon/bluetooth
    container_name: bluetooth
    network_mode: host
    restart: always
    volumes:
      - ./bluetooth:/app 
```


### Related
Thanks to [andrewjfreyer](https://github.com/andrewjfreyer/presence) to make the bluetooth-mqtt script &
thanks to [helto4real](https://github.com/helto4real/hassio) for dockerize this. 