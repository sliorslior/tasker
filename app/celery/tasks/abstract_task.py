from celery import Task
from celery.result import AsyncResult
from app.celery.celery_config import celery

class BaseTask(Task):
    def run(self, params):
        raise NotImplementedError("Subclasses must implement the run method.")

    def get_status(self, task_id):
        task_result = AsyncResult(task_id, app=celery)
        status = task_result.status
        result = task_result.result if task_result.ready() else None
        return {"status": status, "result": result}