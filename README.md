# House to do Project

by Robbie Kinloch

## Project Description

This is an app that contains a list of household tasks that need doing to remind my end users of chores that may have been forgotten. The user can create a task that needs doing to insert it into the list, then be able to check details or delete that specific task.

The app has the following key features:
- Observing all tasks in a list
- Adding a task
- Checking the details of a task
- Deleting a task



## Live Site

- [Live Site](https://level-2-project-house-todo.onrender.com/)

## Supporting Documents

[GH pages site](https://level-2-project-house-todo/)

Task Instructions:
- [Instruction documents](docs/instructions/)

Project Evidence
- [Sprint 0: Project Requirements](docs/evidence/sprint-0-requirements.md)
- [Sprint 1: Prototype Development](docs/evidence/sprint-1-prototype.md)
- [Sprint 2: MVP Development](docs/evidence/sprint-2-mvp.md)
- [Sprint 3: Final System Development](docs/evidence/sprint-3-final.md)
- [Review: Project Final Review](docs/evidence/system-review.md)


## Test Accounts

The following user accounts have been created to demonstrate the features of the system:

Test User 1:
- Username: xxxxx
- Password: xxxxx

Test User 2:
- Username: xxxxx
- Password: xxxxx

No test accounts were needed for my project.


## Technologies Used

- [Flask](https://flask.palletsprojects.com/) as the web framework
- [Python](https://www.python.org/) as the programming language used
- [SQLite](https://sqlite.org/) for the database
- [Jinja2](https://jinja.palletsprojects.com/templates/) for page templating

*For easier reading, the docs are hosted as a [GH Pages site](https://waimea-rjkinloch.github.io/level-2-project-house-todo/)*


## Project Structure

```
├── README.md            # Project README
│
├── requirements.txt     # Python modules required
│
├── app/                 # Flask application
│   │
│   ├── __init__.py      # Routes and app logic
│   │
│   ├── .env             # Environment values
│   │
│   ├── templates/       # Jinja2 templates
│   │   ├── pages/       # Full page templates
│   │   └── partials/    # Reusable template parts
│   │
│   ├── static/          # Files to be served directly
│   │   ├── css/         # CSS stylesheets
│   │   ├── images/      # Images
│   │   └── js/          # Javascript files
│   │
│   ├── db/              # Database files
│   │   ├── config.py    # Database schema & seed data
│   │   └── data.sqlite  # SQLite database
│   │
│   └── helpers/         # Helper files (don't modify)
│
└── docs/                # Project documentation
    ├── guides/          # Helpful guides
    ├── instructions/    # Task instructions
    └── evidence/        # Project evidence
```
