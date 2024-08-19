#!/bin/bash

gunicorn app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

sleep 10

RUN ["./docker/bd.sh"]