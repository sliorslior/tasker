from flask import request
from flask_restful import Resource
# from app.celery.tasks.sum_task import SumTask  # Import your task classes
from celery import current_app
from app.celery.celery_config import celery

TASK_MAPPING = {
    'sum': 'app.celery.tasks.sum_task.sum_task', 
}

class TriggerTask(Resource):
    def post(self):
        try:
            data = request.get_json()
            task_type = data.get('tasktype')
            task_params = data.get('params')

            if not task_type or task_type not in TASK_MAPPING:
                return {"error": "Invalid or missing task type."}, 400

            if not isinstance(task_params, dict):
                return {"error": "Invalid or missing task parameters."}, 400

            task_class = TASK_MAPPING[task_type]

            task = celery.send_task(task_class, kwargs=task_params)
            return {"message": "Task triggered", "task_id": task.id}, 202
        
        except Exception as e:
            return {"error": str(e)}, 500

class TaskStatus(Resource):
    def get(self):
        try:
            data = request.get_json()
            task_id = data.get('task_id')
            task_result = current_app.AsyncResult(task_id)
            status = task_result.status
            result = task_result.result if task_result.ready() else None
            return {"status": status, "result": result}, 200

        except Exception as e:
            return {"error": str(e)}, 500