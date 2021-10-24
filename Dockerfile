# This base image uses Debian operating system
FROM python:3.8.0-slim

# This forces python to not buffer output / error
ENV PYTHONUNBUFFERED 1

# This is where we will copy all our code
# Workdir creates the directory if it doesn't exist
WORKDIR /opt

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip &&  pip install --no-cache-dir -r requirements.txt

# in such a way that every component is isolated from each other
COPY . .
