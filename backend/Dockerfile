FROM python:3.9

RUN apt-get update \
    && apt-get install -y postgresql-client \
    && pip install psycopg2-binary alembic

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

CMD ["./docker/app.sh"]





