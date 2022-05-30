FROM python:3.10-alpine

WORKDIR /code

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY /src/app.py /code

CMD ["python3", "app.py"]

