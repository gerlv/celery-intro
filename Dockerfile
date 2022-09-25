FROM python:3.10.6 as requirements-stage

WORKDIR /tmp
RUN pip install poetry==1.2.1
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10.6
WORKDIR /code
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./celery_intro /code/celery_intro
CMD ["celery", "-A", "celery_intro", "--loglevel", "INFO"]
