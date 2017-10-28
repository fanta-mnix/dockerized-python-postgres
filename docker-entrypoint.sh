#!/usr/bin/env bash
set -e

./setup.py
./seed.py

exec "$@"