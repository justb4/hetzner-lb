# PoC Hetzner Load Balancer

PoC to investigate using an Hetzner Load Balancer (LB) with:

* Two backend services `myapp` with FastAPI
* Hetzner private network
* Traefik in backend servers
* TLS endpoint in LB

need to figure out how this works in particular when using HTTPS and
(sub)domains. Is this preserved towards backend? Does CORS still work?

