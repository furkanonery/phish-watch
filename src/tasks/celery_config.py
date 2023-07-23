from celery import Celery
from datetime import timedelta
import os
from dotenv import load_dotenv
from celery.utils.log import get_task_logger

load_dotenv()

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

celery_app = Celery(
    "phish_url_watch_service",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
    include=["phish_tank"]
)

celery_app.conf.beat_schedule = {
    "run_every_six_hours": {
        "task": "phish_tank.get_phish",
        "schedule": timedelta(hours=6),
    },
}

celery_app.conf.timezone = "UTC"
logger = get_task_logger(__name__)
