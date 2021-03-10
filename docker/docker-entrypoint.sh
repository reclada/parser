#!/usr/bin/env bash

set -e

if [ "$1" = 'job' ]; then
  exec reclada-csv-parser $FILENAME
fi

exec "$@"
