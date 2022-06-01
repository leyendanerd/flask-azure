FROM python:3.10-alpine

WORKDIR /code

COPY requirements.txt /requirements.txt

RUN python -m pip install --upgrade pip

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

RUN pip install mysqlclient
RUN pip install python-dotenv

RUN apk del build-deps

RUN pip install -r /requirements.txt

COPY /src/. /code

CMD ["python3", "index.py"]

