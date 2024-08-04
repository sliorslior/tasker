from celery import Celery

def make_celery(app_name=__name__):
    # Using the `memory` backend and broker for local development
    return Celery(app_name, backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

celery = make_celery()