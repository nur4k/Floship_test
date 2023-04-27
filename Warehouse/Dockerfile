FROM python:buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /warehouse

ADD poetry.lock pyproject.toml /warehouse/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --only main

COPY . .

ENTRYPOINT ["gunicorn", "core.wsgi", "--bind", "0.0.0.0:8001", "--workers", "4", "--threads", "4"]
