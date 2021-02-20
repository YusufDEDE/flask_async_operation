from .models import Task
from . import create_app, rq
from tabulate import tabulate
from datetime import datetime as dt
from .utils.crud_actions import CrudAction

crud_action = CrudAction(Task)
app = create_app()


@rq.job
def list_task_record():
    with app.app_context():
        tasks = crud_action.read()
        table = []
        for task in tasks:
            table.append([task.id, task.name, task.priority, task.status, task.created])

        return tabulate(table, headers=["#", "Name", "Priority", "Status", "Created"])


@rq.job
def create_task_record(name, priority):
    with app.app_context():
        return crud_action.create({
            'name': name,
            'priority': priority,
            'status': 'test',
            'created': dt.now(),
        })


@rq.job
def delete_task_record(task_id):
    with app.app_context():
        return crud_action.delete(task_id)
