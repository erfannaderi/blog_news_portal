import os
from datetime import timedelta

from celery import Celery

CELERY_LOG_LEVEL = 'INFO'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_news_portal_project.settings")
app = Celery("blog_news_portal_project")
app.conf.update(
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/0',
    task_always_eager=False,
    worker_concurrency=1000,
    worker_pool='eventlet',
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    timezone='UTC',

)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.conf.beat_schedule = {
    'my-scheduled-task': {
        'task': 'news.tasks.fetch_data',
        'schedule': timedelta(days=1),  # Replace with your desired schedule
    },
}
# command for celery
# comande run servero begir bad ina
# celery -A blog_news_portal_project beat -l info
# celery -A blog_news_portal_project worker -l info --concurrency=1000 --pool=eventlet
