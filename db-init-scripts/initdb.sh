#!/usr/bin/bash

# if there is an initial database, load the initial db automatically
# put the backup in db/pgsql_backup
# the backup can be created by running "pg_dump -Fc omnianalytics_db > pgsql_backup"

DB_NAME=pretest_db

echo "###";
echo "# Create Db";
echo "###";
createdb -U postgres ${DB_NAME}

echo "###";
echo "# Refeed Data";
echo "###";
pg_restore -U postgres -O -Fc --dbname=${DB_NAME} < /db/demo_db