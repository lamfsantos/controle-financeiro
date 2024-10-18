#!/bin/bash
# wait-for-mysql.sh

set -e

host="$1"
shift
cmd="$@"

until mysql -h"$host" -uroot -pexample -e "SELECT 1" > /dev/null 2>&1; do
  >&2 echo "MySQL is unavailable - waiting..."
  sleep 2
done

>&2 echo "MySQL is up - executing command"
exec $cmd
