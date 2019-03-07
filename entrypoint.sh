#!/bin/sh

crond -b

cd $WORKSPACE && /usr/local/bin/gunicorn -c $WORKSPACE/deploy/gunicorn_config.py thor.wsgi:application
