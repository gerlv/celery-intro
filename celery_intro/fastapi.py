from fastapi import FastAPI
from celery_intro.tasks import say
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/say/{message}")
def schedule_say(message):
    say.delay(message=message)
    return {"status": "ok"}
