#!/usr/bin/env bash

# Lauching API server

cd backend && docker-compose up -d --build

# Lauching React server

cd ../frontend && docker-compose up -d --build