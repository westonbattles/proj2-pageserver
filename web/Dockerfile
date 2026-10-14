#python 3.14 bangggg
FROM python:3.14
MAINTAINER Weston Battles "wbattles@uoregon.edu"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
