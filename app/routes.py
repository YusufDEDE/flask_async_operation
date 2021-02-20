"""Application routes."""
from datetime import datetime as dt

from flask import current_app as app
from flask import make_response, redirect, render_template, request, url_for

from .models import Task, db


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
        new_task = Task(
            name=name,
            priority=priority,
            status="True",
            created=dt.now(),
        )  # Create an instance of the User class
        db.session.add(new_task)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        redirect(url_for("task_records"))
    return render_template("task.jinja2", tasks=Task.query.all(), title="Show Task")
