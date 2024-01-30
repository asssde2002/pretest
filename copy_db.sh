#!/bin/bash

docker-compose exec db sh -c 'pg_dump -U postgres -Fc pretest_db > /tmp/demo_db'

if [ $? -eq 0 ]; then
    # 複製備份文件到主機
    docker-compose cp db:/tmp/demo_db db/demo_db
    echo "Backup completed successfully."
else
    echo "Backup failed."
fi