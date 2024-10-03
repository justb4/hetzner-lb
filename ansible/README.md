# Maintain with Ansible

Ansible is used to install, configure and maintain the entire server.

## Virtualenv

On your local system install ansible (a v2 version) in virtual env.
For example:


```
pyenv activate ansible-python-3.7.1
pip install ansible
pyenv rehash
```

Check:

```
pip freeze | grep ansible
ansible==10.4.0
ansible-core==2.17.4
```

## Key management

```
ssh-keygen -t rsa -q -N "" -f vars/key.rsa

```

## Install required Roles

Here in local dir `roles` :

```

mkdir roles
ansible-galaxy install --roles-path ./roles -r requirements.yml

```

## Bootstrap

### Pre on server

* create Hetzner VM server, server name `MYSERVER-1`
* paste your SSH public key (no password access)

### Bootstrap OS
```

# Bootstrap servers with Ubuntu core packages
ansible-playbook -v bootstrap.yml -i hosts/prod.yml

```

## Test if working

Basic sanity test:

```
ansible-playbook -v  test.yml -i hosts/prod.yml


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

Manage the remote Host OS (Ubuntu) system.

```
ansible-playbook -v  system.yml -i hosts/prod.yml --tags update_packages

ansible-playbook -v  system.yml -i hosts/prod.yml --tags reboot

```
