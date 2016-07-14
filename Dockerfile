FROM ubuntu:16.04

RUN apt-get update && apt-get install python2
RUN apt-get install python-dev python-pip
RUN pip install -U pip && pip install django
ADD . /www-data
EXPOSE 8000
CMD ["python", "/www-data/manage.py", "runserver"]
