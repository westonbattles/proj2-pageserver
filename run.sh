docker rm -f $(docker ps -aq)
docker build -t uocis-flask-demo ./web
docker run -p 6767:5000 uocis-flask-demo