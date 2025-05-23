FROM python:latest

RUN python --version

WORKDIR /code

COPY . .

RUN apt update

# RUN python -m pip install --upgrade pip

RUN python -m pip install \
  python-dotenv \
  boto3 \
  requests

ENTRYPOINT [ "python", "spotify.py" ]