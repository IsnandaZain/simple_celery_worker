from celery import celery

from configuration import CeleryConfig
from worker.libs import module


app = Celery(__name__)
app.config_from_object(CeleryConfig)

module.walk_modules("worker")