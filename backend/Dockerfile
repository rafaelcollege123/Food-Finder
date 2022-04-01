FROM python:3.10.1-slim-buster

WORKDIR /usr/app

RUN apt-get update \
  && apt-get -y install gcc \
  && apt-get clean

RUN pip install --upgrade pip
RUN pip install poetry
COPY pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev  

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "foodfinder.wsgi"]