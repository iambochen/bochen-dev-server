from celery import Celery

app = Celery(
    'bochen_dev_server',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0',
    include=['worker.tasks']
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Asia/Taipei',
    enable_utc=True,
    worker_concurrency=4,  # Number of worker processes
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 minutes
    broker_connection_retry_on_startup=True,
    result_expires=3600,  # Results expire after 1 hour
)
