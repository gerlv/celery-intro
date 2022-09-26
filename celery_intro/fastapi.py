from time import sleep
from fastapi import FastAPI
from celery_intro.tasks import say, slow_process, retry_three_times

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/say/{message}")
def schedule_say(message):
    say.delay(message=message)
    return {"status": "ok"}


@app.get("/retry")
def retry():
    retry_three_times.delay()
    return {"retry": True}


@app.get("/fast")
def fast():
    slow_process.delay()
    return {"good": True}


@app.get("/slow")
def slow():
    sleep(5)
    return {"good": False}
