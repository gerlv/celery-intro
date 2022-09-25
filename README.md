# Celery

## How to run

```bash
docker compose up
```

This will build and start all containers.

Visit [http://localhost:8080](http://localhost:8080)

## Celery tasks

```python
from celery_intro.tasks import *

say.delay("some message")
get_my_ip.delay()
retry_three_times.delay()  # retry 3 times
```

## Celery Beat

Runs `say.delay("repeat every 30 seconds...")` every 30 seconds.

## Web Endpoints

- [http://localhost:8080](http://localhost:8080) - 
- [http://localhost:8080/slow](http://localhost:8080/slow) - 5s delay of the response
- [http://localhost:8080/fast](http://localhost:8080/fast) - Simple response
- [http://localhost:8080/say/hello](http://localhost:8080/say/hello) - Schedule celery task
