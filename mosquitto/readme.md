# MQTT
Docker container for mqtt broker


## Generate a mosquitto pw_file
Change the secrets in home-assistant to match your username and password
`$ docker exec -it mqtt sh`

and then
`$ mosquitto_passwd -c /mosquitto/config/pwfile <username>`

