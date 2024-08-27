FROM python:3.9-slim

RUN apt-get update && apt-get install -y python3-distutils

RUN mkdir -p /var/app
WORKDIR /var/app
COPY . /var/app

RUN pip install --upgrade pip setuptools==58.0.4 wheel six

# install scipy & numpy
# install required packages
RUN pip install scipy numpy==1.21.0

RUN python3 -m pip install --upgrade setuptools wheel
RUN pip install .
