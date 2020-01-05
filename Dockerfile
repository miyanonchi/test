FROM python:3

WORKDIR /testapp
CMD ["python", "./app.py"]

ADD app /testapp

RUN pip install -r requirements.txt
