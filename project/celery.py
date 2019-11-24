from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms, shared_task
# from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('sheingor_backend')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# 允许root 用户运行celery
platforms.C_FORCE_ROOT = True


@app.task(bind=True, max_retries=3, autoretry_for=(Exception,))
def debug_task(self):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    aaaa
    print('Request: qqqqqqqqqqq')


# app.conf.update(
#     CELERYBEAT_SCHEDULE = {
#         'sum-task': {
#             'task': 'api.tasks.add',
#             'schedule': crontab(minute='*'),
#             'args': (14, 25)
#         }
#     }
# )
