Container Example!
===================

A simple example of using a container and docker compose with a python
application.

## Installation steps for Ubuntu

```
$ sudo apt-get install linux-image-extra-$(uname -r) linux-image-extra-virtual
$ sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo apt-key fingerprint 0EBFCD88
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
$ sudo apt-get update
$ sudo apt-get install docker-ce
$ sudo curl -o /usr/local/bin/docker-compose -L "https://github.com/docker/compose/releases/download/1.11.2/docker-compose-$(uname -s)-$(uname -m)"
$ sudo chmod +x /usr/local/bin/docker-compose
$ docker-compose -v
$ sudo gpasswd -a $USER docker
$ sudo service docker restart
$ newgrp docker
```

## Run


To execute docker compose follow the following steps

1. Define your app's environment with a Dockerfile so it can be reproduced anywhere.
2. In a file `docker-compose.yml` describe the specification of its different containers with their respective properties.
3. Run `docker-compose up --build` and Build will start and run the images of all containers.
4. Finally, run docker compose-up to run your entire application.


Install `docker` and `docker-compose` then simply:

    docker-compose up

Then you can go to [http://0.0.0.0/ping](http://0.0.0.0/ping).

