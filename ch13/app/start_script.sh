#!/bin/bash
source activate sentiment-app 
GUNICORN_CMD_ARGS="--access-logfile -" gunicorn -w 3 -b :5000 -t 5 -k uvicorn.workers.UvicornWorker main:app -
