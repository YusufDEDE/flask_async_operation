"""App entry point."""
from app import create_app
from flask_script import Manager, Command, Option
from datetime import datetime as dt
from app.models import Task
from app.utils.crud_actions import CrudAction
from tabulate import tabulate


crud_action = CrudAction(Task)
app = create_app()
manager = Manager(app)


@manager.command
def create_task(name, priority):
    crud_action.create({
        'name': name,
        'priority': priority,
        'status': 'adad',
        'created': dt.now(),
    })

    print("uloos ", name, priority)


@manager.command
def list_task():
    tasks = Task.query.all()
    table = []
    for task in tasks:
        table.append([task.id, task.name, task.priority, task.status, task.created])

    print(tabulate(table, headers=["#", "Name", "Priority", "Status", "Created"]))


if __name__ == "__main__":
    manager.run()
