# Traefik

Traefik is used for reverse proxy.

### Preperations

Traefik container depens on two variables, defined in `.env` file that should be created on same level as docker-compose file, these variables are `EMAIL` and `DOMAIN`.

```
$ sudo touch .env
$ echo "EMAIL=<redacted>" | sudo tee -a .env
$ echo "DOMAIN_=<redacted>" | sudo tee -a .env
```

