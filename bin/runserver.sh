#!/bin/bash

SCRIPT_DIR=$( cd "$( dirname "$0" )" && pwd )
stty -echo
read -p "Database Password: " PASSWORD; echo
stty echo
export DATABASE_URL=postgres://${USER}:${PASSWORD}@localhost/beerandme
python $SCRIPT_DIR/../manage.py runserver localhost:8080

