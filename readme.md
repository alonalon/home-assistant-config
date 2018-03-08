# Home Assistant Configuration
> My Home Assistant Configuration


### Setups

#### Google assistant

Go to [Cloud console](https://console.cloud.google.com/) create a new api, if you already have a working one, use that. Enable HomeGraph Api and create an api key and copy.
Create a new project in [Developer console](https://console.actions.google.com/), select the same that your api have, to share project id.

Download the gactions file to a folder on the host, use wget. change rights to make it executable with `chmod +x gactions`.

Follow the instuctions on the [Docs](https://home-assistant.io/components/google_assistant/)

#### Owntracks

Setup [Bridge](https://geekvisit.com/home-assistant-mosquitto-mqtt-cloudmqtt-work-mqtt-bridge/)for external & mosquitto
