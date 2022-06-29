FROM python:3.10-alpine

WORKDIR /code

COPY /src/requirements.txt /requirements.txt

RUN python -m pip install --upgrade pip

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

RUN pip install sentry-sdk
RUN pip install --upgrade 'sentry-sdk[flask]'

# RUN pip install mysqlclient  #si es con mysql 
RUN pip install python-dotenv
RUN pip install psycopg2-binary

RUN apk del build-deps

RUN pip install -r /requirements.txt

COPY /src/. /code

CMD ["python3", "index.py"]

