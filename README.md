# Basic Development Environment with DOcker

### Overview
This repo contains basic setup for development with docker.

The setup contains development environment for node.js & python as backend.
To ease development it sets:
- Volumes: by default docker does not contain persistence storage. In order to allow persistenance storage volumes is needed. Volumes gives us a way to map our local directory to directory inside of docker
- Hot reloading
  --> In node.js this is achieved by nodemon
  --> In python flask, this is achieved by setting the FLASK_ENV=development

### Important docker command
1) To build & start docker image in the background
  `docker-compose up --build -d`
2) To show logs from a specific service
  `docker-compose logs -f <service_name>`
3) To ssh into a particular service
  `docker-compose exec <service_name> bash`
  In alpine version, bash is not available, so we need to use sh
  `docker-compose exec <service_name> /bin/sh`
4) To remove all docker containers
  `docker rm $(docker ps -a -q) -f`
5) To remove all docker images
  `docker rmi $(docker images) -f`