# Appdaemon
Appdaemon apps are connected to home-assistant

Appdaemon needs a few variables to be setup

```
ha_url: https://home-assistant:8123 (url to your home-assistant)
ha_token: abcdef (long-lived token in home-assistant)
base_latitude: 1234
base_longitude: 1234
base_elevation: 0
base_time_zone: Europe/Stockholm
```

#### Presence
shamefully copied precense and helpers from [Thomas Loven](https://github.com/thomasloven/)
Adds a new device.tracker entity with states `just_arrived` and `just_left` in additional to regular `home`, `away`
Looking only on source `gps` for now.


