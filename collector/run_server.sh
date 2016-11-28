#!/bin/bash

gunicorn --bind 0.0.0.0:8000 --backlog 2048 --workers 1 --threads 1 --worker-connections 100 --max-requests 1000 \
         --timeout 60 --graceful-timeout 60 --keep-alive 5 collector.app:api
