#!/bin/bash

export HOST_HOSTNAME=$(hostname)
docker compose rm --force --stop
