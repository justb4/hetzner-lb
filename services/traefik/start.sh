#!/bin/bash

# Stop and remove possibly old containers
./stop.sh

docker compose up -d
