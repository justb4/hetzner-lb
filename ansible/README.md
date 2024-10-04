# Maintain with Ansible

Ansible is used to install, configure and maintain the entire server.

## Virtualenv

On your local system install Ansible in virtual env.
For example using Python 3.12.3:


```
pyenv virtualenv 3.12.3 ansible-3.12.3
pyenv activate ansible-python-3.12.3
pip install ansible
pyenv rehash
```

Check Ansible version:

```
pip freeze | grep ansible
ansible==10.4.0
ansible-core==2.17.4
```

## Key management (for GH Workflows)

```
ssh-keygen -t rsa -b 4096 -q -N "" -f vars/sshkey.rsa

```
**IMPORTANT: move vars/sshkey.rsa to save place!! Only keep vars/sshkey.rsa.pub !**

Open https://github.com/justb4/hetzner-lb/settings/secrets/actions. Create new secret
`ANSIBLE_SSH_PRIVATE_KEY` with content of `sshkey.rsa`.

## Setup

Hetzner: VMs and LB in private network.
Local config SSH file.

## Install required Ansible Roles

Here in local dir `roles` :

```
cd ansible
mkdir roles
ansible-galaxy install --roles-path ./roles -r requirements.yml

```

## Bootstrap

### Pre on Hetzner Console

* create Hetzner VM servers, names `myserver-1`, `myserver-2`
* hostnames will be from [hosts YAML](hosts/prod.yml)
* paste your SSH public key (no password access)

### Bootstrap OS
```

# Bootstrap servers with Ubuntu core packages
ansible-playbook -v bootstrap.yml -i hosts/prod.yml

# if first time connecting (IP not yet in known_hosts)
# Are you sure you want to continue connecting (yes/no/[fingerprint])
# hit return
```

## Test if working

Basic sanity test:

```
ansible-playbook -v  test.yml -i hosts/prod.yml

# Test if you can login with generated key after bootstrap
ssh -i <saved_path>/sshkey.rsa myuser@myserver1
```

## Install

Install all services/apps (commit to GH first!):

```
ansible-playbook -v install.yml -i hosts/prod.yml

```

## Deploy

Deploy individual services:

```
ansible-playbook -v  deploy.yml -i hosts/prod.yml --tags traefik

ansible-playbook -v  deploy.yml -i hosts/prod.yml --tags myapp

```

## Global Service

Manage `systemd` service:

```
ansible-playbook -v  service.yml -i hosts/prod.yml --tags status

ansible-playbook -v  service.yml -i hosts/prod.yml --tags stop

ansible-playbook -v  service.yml -i hosts/prod.yml --tags start

```

## System Management

Manage the remote (Ubuntu) system.

```
ansible-playbook -v  system.yml -i hosts/prod.yml --tags update_packages

ansible-playbook -v  system.yml -i hosts/prod.yml --tags reboot

```
