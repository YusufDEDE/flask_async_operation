from app import create_app
from app.models import Task
from tabulate import tabulate
from datetime import datetime as dt
from app.utils.crud_actions import CrudAction
from flask_script import Manager, Command


crud_action = CrudAction(Task)
app = create_app()
manager = Manager(app)


@manager.command
def create_task(name, priority):
    result = crud_action.create({
        'name': name,
        'priority': priority,
        'status': 'adad',
        'created': dt.now(),
    })

    print(result)


@manager.command
def list_task():
    tasks = crud_action.read()
    table = []
    for task in tasks:
        table.append([task.id, task.name, task.priority, task.status, task.created])

    print(tabulate(table, headers=["#", "Name", "Priority", "Status", "Created"]))


@manager.command
def delete_task(task_id):
    result = crud_action.delete(task_id)
    print(result)


if __name__ == "__main__":
    manager.run()
