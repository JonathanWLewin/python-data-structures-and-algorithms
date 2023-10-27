# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install flask

COPY . .

CMD ["flask", "--app=pyrefine", "run", "--host=0.0.0.0"]