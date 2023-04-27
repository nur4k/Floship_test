FROM python:buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /store

ADD poetry.lock pyproject.toml /store/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --only main

COPY . .

ENTRYPOINT ["gunicorn", "core.wsgi", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "4"]