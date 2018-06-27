# Generate a mosquitto pw_file
`$ mosquitto_passwd -b config/pwfile USERNAMEGOESHERE PASSWORDGOESHERE`

# Check if pw_file has encrypted the password
`$ cat config/pwfile USERNAMEGOESHERE:$6$UAAK5576QTPkld45$/wi/FPzXI0fxZg40Km//dqHyA+sBMWLjvLaQtjuFS0FODXry4KE1vJji3YbbtehYlZRWOqfORltkwVmLzq8sfA==`

# Make sure folders are executable and create logfile
`$ chmod -R 770 config/ data/ log/`
`$ touch log/mosquitto.log`
