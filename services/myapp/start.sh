#!/bin/bash

./stop.sh
export HOST_HOSTNAME=$(hostname)
docker compose up -d
