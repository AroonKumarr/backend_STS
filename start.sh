#!/bin/bash

echo "Starting Token API..."
uvicorn token_server:app --host 0.0.0.0 --port 8000 &

echo "Starting LiveKit Agent..."
python agent.py dev
