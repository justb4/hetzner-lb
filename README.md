# PoC Hetzner Load Balancer

PoC to investigate using an Hetzner Load Balancer (LB) for the following items/issues/questions:

* [x] Overall working
* [x] Hetzner private network, howto
* [x] Hetzner private network VMs: SSH access from outside (stepping stone VM + .ssh/config with `ProxyJump`)
* Attaching Hetzner Dedicated servers to private network (vSwitch)
* Hetzner private network VMs: Ansible access from GitHub Workflows
* TLS endpoint in LB with external DNS
* [x] Backend services: is Real URL propagated?
* Backend services: Traefik routing, can we use subdomains?
* [x] Backend services: is Real Client IP propagated?
* [x] Backend Traefik access log: is Real Client IP logged (for metering) ?
* Backend services: how to enable CORS?

## Setup

Two backend servers (VMs) and one Hetzner LoadBalancer.

Each VM runs Ubuntu 24.04 with Docker.
Two Docker Containers are running: a [Traefik frontend](services/traefik/docker-compose.yml) proxy and single FastAPI [myapp](services/myapp/src/main.py) 
backend service that returns request info for analysis.

VMs and LB are acquired in Hetzner console dashboard.
VMs are quickly [bootstrapped](ansible/bootstrap.yml) and [installed](ansible/install.yml) using Ansible.
Each VM runs a [systemd service](ansible/templates/systemd.service.j2) such that all Docker Containers are started at reboot.

TODO: use Terraform/OpenTofu for provisioning all resources (VMs, LB, networks etc)
