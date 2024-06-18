#!/bin/bash
web: gunicorn app:app --host 0.0.0.0 --port $PORT
rq worker --with-scheduler
