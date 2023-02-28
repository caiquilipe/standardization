FROM python:3.11.1-alpine3.17

ENV DockerHOME=/home/project/standardization

RUN mkdir -p $DockerHOME 
WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN pip install --upgrade pip 

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev


COPY . $DockerHOME 

RUN pip install -r requirements.txt 

ENV C_FORCE_ROOT=1
# start server  
CMD ["python", "manage.py", "runserver"]
