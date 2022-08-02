FROM python:latest

ENV FLASK_APP=app.py

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host","0.0.0.0"]