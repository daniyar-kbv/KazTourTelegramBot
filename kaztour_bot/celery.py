import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kaztour_bot.settings')

app = Celery('kaztour_bot', broker=os.environ.get('BROKER_URL', 'amqp://localhost'), backend='rpc://', )
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()