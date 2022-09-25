import logging
import requests
from celery_intro.celery import app

LOGGER = logging.getLogger(__name__)


@app.task
def say(message):
    LOGGER.info(f"Message: {message}")


@app.task
def get_my_ip():
    response = requests.get("https://api.ipify.org?format=json")
    LOGGER.info(f"Response: {response.json()}")


@app.task(
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 3, "default_retry_delay": 5},
    retry_backoff=True,
)
def retry_three_times():
    response = requests.get("https://httpbin.org/status/404")
    LOGGER.info(f"Status code: {response.status_code}")
    response.raise_for_status()
