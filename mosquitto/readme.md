# Generate a mosquitto pw_file
After the mqtt container is started run

`$ docker exec -it mqtt sh`

and then 
`$ mosquitto_passwd -c /mosquitto/config/pwfile username`

# Make sure folders are executable and create logfile
`$ chmod -R 770 config/ data/ log/`
`$ touch log/mosquitto.log`
