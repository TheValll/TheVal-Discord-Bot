FROM python:3.9
RUN apt-get update

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app/ ./

ENTRYPOINT ["sh", "entrypoint.sh"]
