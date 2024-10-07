# PoC Hetzner Load Balancer

PoC to investigate using an Hetzner Load Balancer (LB) for the following items/issues/questions:

* [x] Overall working
* [x] Hetzner private network, howto
* [x] Hetzner private network VMs: SSH access from outside (stepping stone VM + .ssh/config with `ProxyJump`)
* [x] Hetzner private network VMs: how to access (internet) outside subnets
* [x] Attaching Hetzner Dedicated servers to private network (vSwitch)
* [x] Attaching Hetzner Dedicated servers to Load Balancer
* [x] Firewalling Dedicated servers for all incoing, only access via LB and Stepstone
* [x] Hetzner private network VMs: Ansible access from GitHub Workflows
* [x] TLS endpoint in Load Balancer with Hetzner DNS
* [x] Backend services: is Real URL propagated?
* [x] Backend services: Traefik routing, using subdomains.
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

## Gotchas

* when using Hetzner Private Network, VMs cannot connect outside subnets (need router VM or use Primary IP with Firewall)
* steps for dedicated server with vSwitch are quite involved, see  [tutorial](https://docs.hetzner.com/cloud/networks/connect-dedi-vswitch/).
* last step adding line in `#/etc/systemd/network/10-enp0s31f6.network` appeared not neccessary (file did not exist)
