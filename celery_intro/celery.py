from celery import Celery

app = Celery(broker="amqp://guest:guest@rabbitmq:5672", include=["celery_intro.tasks"])

app.conf.beat_schedule = {
    "say-every-2-seconds": {
        "task": "celery_intro.tasks.say",
        "schedule": 30.0,
        "args": ("repeat every 30 seconds...",),
    },
}
