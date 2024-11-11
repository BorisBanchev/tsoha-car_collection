# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.10.12

FROM python:${PYTHON_VERSION}-slim

LABEL fly_launch_runtime="flask"

WORKDIR /code

ENV DATABASE_URL="postgresql://user:secret@localhost:5432/mydatabasename"
ENV SECRET_KEY=<salainen-avain>
ENV FLY_DEPLOYMENT=False

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip install psycopg2-binary
COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]
