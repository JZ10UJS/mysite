FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python2.7
RUN apt-get install -y python-dev python-pip python-setuptools
RUN pip install -U pip && pip install django==1.8.3
ADD . /www-data
EXPOSE 8000
CMD ["python", "/www-data/manage.py", "runserver", "0.0.0.0:8000"]
