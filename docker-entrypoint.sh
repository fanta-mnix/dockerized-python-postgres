#!/usr/bin/env bash
set -e

./seed.py

exec "$@"