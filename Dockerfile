FROM python:3.7-alpine3.8

ENV WORKSPACE=/workspace
ENV PYTHONPATH="$WORKSPACE"
ENV LC_ALL="en_US.UTF-8"
ENV LANG="en_US.UTF-8"
ENV THOR_HOST="0.0.0.0"
ENV THOR_PORT="5000"
ENV THOR_GUNICORN_WORKERS="1"

RUN mkdir $WORKSPACE
WORKDIR $WORKSPACE

COPY ./entrypoint.sh /entrypoint.sh
COPY ./requirements.txt /tmp/requirements.txt
COPY ./thor $WORKSPACE/thor
COPY ./deploy $WORKSPACE/deploy
RUN chmod +x /entrypoint.sh

RUN apk add --no-cache python3-dev mariadb-dev build-base 
RUN pip3 install -i https://pypi.douban.com/simple -r /tmp/requirements.txt
RUN pip3 install -i https://pypi.douban.com/simple gunicorn
RUN apk del python3-dev mariadb-dev build-base &&\
RUN apk add mariadb-client-libs

ENTRYPOINT "/entrypoint.sh"
