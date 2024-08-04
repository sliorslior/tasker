from flask import Flask
from flask_restful import Api
from app.config import Config
from app.routes.task import TriggerTask, TaskStatus

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    api = Api(app)
    api.add_resource(TriggerTask, '/tasks/run')
    api.add_resource(TaskStatus, '/tasks/status')

    return app