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
@app.get("/tasks")
def show_all_tasks():
    with connect_db() as db:
        sql = """
            SELECT id, name
            FROM topic
            SELECT id, topic_id, name, urgency
            FROM task
        """
        params = ()
        tasks = db.execute(sql, params).fetchall()

        return render_template("pages/task_list.jinja", tasks = tasks)

#-----------------------------------------------------------
# Details of Task
#-----------------------------------------------------------
@app.get("/task/details")
def show_all_tasks():
    with connect_db() as db:
        sql = """
            SELECT id, name, members
            FROM topic
            SELECT id, topic_id, name, details,  urgency
            FROM task
        """
        params = ()
        tasks = db.execute(sql, params).fetchall()

        return render_template("pages/task_details.jinja", tasks = tasks)
# #-----------------------------------------------------------
# # New Task Form
# #-----------------------------------------------------------
# @app.get("/task/new")
# def show_task_form():
#     return render_template("pages/task_form.jinja")
# #-----------------------------------------------------------
# # Handle the task form data
# #-----------------------------------------------------------
# @app.post("/task/new")
# def process_task_form():
#     # Get the form data
#     species = request.form.get("species", "unknown").strip()
#     name = request.form.get("name", "unknown").strip()

#     # Connect to the db
#     with connect_db() as db:

#         sql = """

#                 INSERT INTO creatures (species,name)
#                 VALUES (?, ?)

#         """
#         params = (species, name)

#         #  Run the query
#         db.execute(sql, params)

#         flash(f"Creature {name} added successfully")

#         # We're done, so back to the list
#         return redirect("/creatures")

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

