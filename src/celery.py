import os
from celery import Celery

os.environ.setdefault(key='DJANGO_SETTINGS_MODULE', value='src.settings')
app = Celery(main='src')  # указывается имя основного модуля в качестве аргумента

app.config_from_object(obj='django.conf:settings',
                       # Определяется файл настроек Django в качестве файла конфигурации для Celery
                       namespace='CELERY')  # и предоставляется пространство имен "CELERY".
app.autodiscover_tasks()
