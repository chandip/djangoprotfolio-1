apk update && apk add git curl

#Create Droplet in Digital Ocean
base=https://github.com/docker/machine/releases/download/v0.16.0 && curl -L $base/docker-machine-$(uname -s)-$(uname -m) >/usr/local/bin/docker-machine && chmod +x /usr/local/bin/docker-machine
docker-machine create --driver digitalocean --digitalocean-access-token 3c9474ad6d5eb467439e9e3e429d17646d6efc03d061bf8655a29a5e844a4044 docker-sandbox

#Pull the ENV for connecting local docker to listen remote docker daemon
eval $(docker-machine env docker-sandbox --shell sh)

#Pull codes in locally
git clone https://github.com/privatejava/djangoprotfolio
cd djangoprotfolio

#Setting environment for building docker locally
DB_NAME=dev_db
DB_USER=dev_user
DB_PASS=6f6dEBZ6GEHA2nw2
DB_HOST=dev-db.cmpakly6j0hy.us-east-2.rds.amazonaws.com
DB_PORT=5432
SUPER_USER=admin
SUPER_EMAIL=maskeyc\@gmail.com
SUPER_PASS=admin9090

#Build the docker image remotely by the help of ENV previously set 
#Docker is now connected to remote docker daemon.
docker build --build-arg DB_HOST=$DB_HOST --build-arg DB_NAME=$DB_NAME --build-arg DB_USER=$DB_USER --build-arg DB_PASS=$DB_PASS --build-arg DB_PORT=$DB_PORT --build-arg SUPER_USER=$SUPER_USER --build-arg SUPER_EMAIL=$SUPER_EMAIL --build-arg SUPER_PASS=$SUPER_PASS -t py-test -f docker/prod/python/Dockerfile .

#Run the docker image remotely 
docker run -p 80:80 py-test


