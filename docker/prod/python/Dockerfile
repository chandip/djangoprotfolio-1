FROM python:3.5-slim
MAINTAINER maskeyc@gmail.com

ARG DB_NAME
ARG DB_USER
ARG DB_HOST
ARG DB_PASS
ARG DB_PORT

ENV DB_NAME=${DB_NAME}
ENV DB_USER=${DB_USER}
ENV DB_HOST=${DB_HOST}
ENV DB_PASS=${DB_PASS}
ENV DB_PORT=${DB_PORT}

COPY ./madzones /madzones

WORKDIR /madzones

RUN pip install --no-cache-dir -r requirements/prod.txt

COPY ./docker/prod/python/entrypoint.sh /entrypoint.sh

RUN python manage.py makemigrations blogs courses pages quizes && python manage.py migrate

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
