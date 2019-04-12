FROM python:3.7.2
LABEL maintainer="maskeyc@gmail.com"

# create app directory
ENV DOCKERIZE_VERSION="0.1.0" \
    PYTHONUNBUFFERED="1" \
    DJANGO_DB_HOST="madzones_protfolio" \
    DJANGO_DB_PORT="5432"
#    DJANGO_SUPERUSER_NAME="chandip" \
#    DJANGO_SUPERUSER_MAIL="maskeyc@gmail.com" \
#    DJANGO_SUPERUSER_PASS="administrator"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/protfolio/madzones/

WORKDIR /usr/src/protfolio/madzones/

COPY requirements.txt /usr/src/protfolio/

COPY . /usr/src/protfolio/madzones/

RUN pip install -r /usr/src/protfolio/madzones/requirements.txt

#CMD ["python", "manage.py", "makemigrations"]

#CMD ["python", "manage.py", "makemigrations blogs courses pages quizes"]

#CMD ["python", "manage.py", "migrate"]



RUN chmod +x /usr/src/protfolio/madzones/entrypoint.sh

ENTRYPOINT ["/usr/src/protfolio/madzones/entrypoint.sh"]

#CMD ["python", "manage.py", "migrate"]

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

VOLUME /usr/src/protfolio/madzones/