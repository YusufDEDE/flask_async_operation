"""Application routes."""
from datetime import datetime as dt

from flask import current_app as app
from flask import make_response, redirect, render_template, request, url_for

from .models import Task, db
from .utils.crud_actions import CrudAction

crud_action = CrudAction(Task)


@app.route("/", methods=["GET"])
def task_records():
    name = request.args.get("user")
    priority = request.args.get("email")
    if name and priority:
        existing_task = Task.query.filter(
            Task.name == name or Task.priority == priority
        ).first()
        if existing_task:
            return make_response(f"{name} ({priority}) already created!")

        crud_action.create({
            'name': name,
            'priority': priority,
            'status': 'True',
            'created': dt.now(),
        })

        redirect(url_for("task_records"))
    return render_template("task.jinja2", tasks=crud_action.read(), title="Show Task")
