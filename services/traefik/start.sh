#!/bin/bash


# Stop and remove possibly old containers
./stop.sh

#sudo mkdir -p ${TRAEFIK_LOG_DIR}
#sudo chown ${TRAEFIK_USER}:${TRAEFIK_USER} ${TRAEFIK_LOG_DIR}

docker compose up -d
