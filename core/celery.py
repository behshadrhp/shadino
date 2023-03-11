import os
from celery import Celery

# local variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# create Celery app
app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks() 