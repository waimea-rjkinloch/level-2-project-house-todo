#===========================================================
# PROJECT NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Task Page - Shows a list of all the tasks.
#-----------------------------------------------------------
@app.get("/")
def show_all_tasks():
    with connect_db() as db:
        sql = """
            SELECT 
                topic.id        AS topic_id, 
                topic.name      AS topic_name,
                task.id         AS task_id, 
                task.name       AS task_name,
                task.urgency    AS task_urgency

            FROM topic
            JOIN task ON task.topic_id = topic.id

            ORDER BY task.urgency DESC
        """
        params = ()
        tasks = db.execute(sql, params).fetchall()

        return render_template("pages/task_list.jinja", tasks = tasks)

#-----------------------------------------------------------
# Details of Task
#-----------------------------------------------------------
@app.get("/task/<int:id>/details")
def show_task_details(id):
    with connect_db() as db:
        sql = """
            SELECT
                topic.id            AS topic_id,
                topic.name          AS topic_name,
                topic.members       AS topic_members,
                task.id             AS task_id,
                task.name           AS task_name,
                task.description    AS task_description,
                task.est_time       AS task_est_time,
                task.complete_by    AS task_complete_by,
                task.urgency        AS task_urgency

            FROM topic
            JOIN task ON task.topic_id = topic.id
            WHERE task.id = ?

        """

        task = db.execute(sql, (id,)).fetchone()

        return render_template("pages/task_details.jinja", task=task)
#-----------------------------------------------------------
# New Task Form
#-----------------------------------------------------------
@app.get("/task/new")
def show_task_form():
    return render_template("pages/task_form.jinja")
#-----------------------------------------------------------
# Handle the task form data
#-----------------------------------------------------------
@app.post("/task/new")
def process_task_form():
    # Get the form data
    topic = request.form.get("topic", "unknown").strip()
    name = request.form.get("name", "unknown").strip()
    description = request.form.get("description", "unknown").strip()
    est_time = request.form.get("est_time", "unknown").strip()
    complete_by = request.form.get("complete_by", "unknown").strip()
    urgency = request.form.get("urgency", "unknown").strip()

    # Connect to the db
    with connect_db() as db:

        sql = """

                INSERT INTO task (topic, name, description, est_time, complete_by, urgency)
                VALUES (?, ?, ?, ?, ?, ?)

        """
        params = (topic, name, description, est_time, complete_by, urgency)

        #  Run the query
        db.execute(sql, params)

        flash(f"Task Added Successfully")

        # We're done, so back to the list
        return redirect("/")

#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

