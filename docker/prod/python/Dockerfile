FROM python:3.5-slim
MAINTAINER maskeyc@gmail.com

COPY ./madzones /madzones

WORKDIR /madzones

RUN pip install --no-cache-dir -r requirements/prod.txt

COPY ./docker/prod/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]