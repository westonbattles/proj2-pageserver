#python 3.14 bangggg
FROM python:3.14 
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
# keep credentials out of app because i think it makes sense?
# RUN mv /app/credentials.ini /credentials.ini

WORKDIR /app
RUN pip install -r requirements.txt
#REMOVE ME
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["python"]
CMD ["app.py"]
