# Traefik

[Traefik](https://traefik.io/traefik/) is the front-end proxy/router.

## Debug Log follow

`docker exec -it traefik tail -f /var/log/traefik/traefik.log` 

## Dynamic File Provider

See `--providers.file.directory=/etc/traefikdyn` in docker-compose.yml.
These are under [dynconfig](dynconfig) and mapped to Traefik container `/etc/traefikdyn`
TLS options seem only be possible (in Docker) via Traefik File Provider.
