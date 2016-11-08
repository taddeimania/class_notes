import time
import random
import datetime
import requests


from celery import Celery

app = Celery('tasks')


@app.task
def cal_decombobulator_xy():
    now = datetime.datetime.now()
    time.sleep(random.randint(5, 10))
    print(now)

@app.task
def kill_joel():
    requests.get("http://10.0.10.221:8000")
