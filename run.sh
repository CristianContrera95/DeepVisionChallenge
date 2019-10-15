#!/bin/bash

DOCKER_NAME='cristian_contrera'

is_docker=$(sudo docker images | grep $DOCKER_NAME | wc -l)

if [ $(( $is_docker )) == 0 ];
then
	echo "Build docker"
	docker build -t $DOCKER_NAME .
fi

echo "docker run --user $UID -v $PWD/:/usr/src/app -it --entrypoint python $DOCKER_NAME src/main.py $1 $2"
