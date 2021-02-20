from time import sleep
from app import create_app
from app.models import Task
from flask_script import Manager, Command
from app.utils.crud_actions import CrudAction
from app.jobs import create_task_record, list_task_record, delete_task_record
from rq.cli import cli

crud_action = CrudAction(Task)

app = create_app()
manager = Manager(app)


@manager.command
def create(name, priority):
    new_record = create_task_record.queue(
        name,
        priority
    )
    sleep(2)
    print(new_record.result)


@manager.command
def lists():
    print("List Task Loading..")
    _lists = list_task_record.queue()
    sleep(2)
    print(_lists.result)


@manager.command
def delete(task_id):
    record = delete_task_record.queue(task_id)
    sleep(2)
    print(record.result)


@manager.command
def q_lists():
    print(cli.resume())


if __name__ == "__main__":
    manager.run()
