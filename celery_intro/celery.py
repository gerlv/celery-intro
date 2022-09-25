from celery import Celery
app = Celery(
    broker='amqp://guest:guest@rabbitmq:5672',
    include=[
        'celery_intro.tasks'
    ]
)

app.conf.beat_schedule = {
  'refresh': {}
}
