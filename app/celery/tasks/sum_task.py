from app.celery.tasks.abstract_task import BaseTask
from app.celery.celery_config import celery

@celery.task(base=BaseTask)
class SumTask(BaseTask):
    def run(self, params):
        result = params.get('a') + params.get('b')
        return result