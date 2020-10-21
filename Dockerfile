FROM python:3.8-alpine

COPY ./sayhello.py /danapp/hello_test.py

WORKDIR /danapp

RUN pip install flask

CMD ["python", "hello_test.py"]