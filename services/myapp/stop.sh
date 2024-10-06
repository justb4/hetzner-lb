#!/bin/bash

export HOST_HOSTNAME=$(hostname)
docker compose down --remove-orphans
