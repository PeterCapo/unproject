<a href="https://codeclimate.com/github/PeterCapo/unproject/maintainability"><img src="https://api.codeclimate.com/v1/badges/a00cd6fcca4971755dc8/maintainability" /></a>
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
![license](https://img.shields.io/github/license/mashape/apistatus.svg)
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/0ce6e75c10d41ae8f3b7)

# API Documentation
https://documenter.getpostman.com/view/5180768/S1a1bUNs?version=latest

# Heroku Link
https://unvexam.herokuapp.com/

# How it Works
- User can signin the app. 
- User can get all projects
- User can get a specific project via project id.
- User can get a specific project via the status of the project. 
- User can create a new project.
- User can update an existing project.
- User can delete an existing project.


## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)

## Installation and Setup

Clone the repository below

```
git clone -b unv https://github.com/PeterCapo/unproject.git
```
# Create a virtual environment

    -virtualenv venv --python=python3.6


# Create a .env file

    $ touch .env

    Set the environment variables

    -export FLASK_APP="run.py"
    -export APP_SETTINGS="development"
    -export JWT_SECRET_KEY="JWT_SECRET_KEY"
    -export DATABASE_URL="dbname='flask_api' host='localhost' port='5432' user='postgres' password='postgres'"



# Install required Dependencies

    pip install -r requirements.txt

# Run the .env file

    source .env

# Endpoints Available

| Method | Endpoint                         | Description                           | 
| ------ | -------------------------------  | ------------------------------------- | 
| POST   | /api/v2/login                    | User login                            | 
| POST   | /api/v2/project                  | User creates new project              | 
| GET    | /api/v2/project                  | User gets all  projects               | 
| GET    | /api/v2/projects/status/completed| User gets specific project with complete status            | 
| GET    | /api/v2/projects/<{id}>          | User gets specific project  using  ID#|  
| PUT    | /api/v2/projects/<{id}>          | User updates a project                | 
| DEL    | /api/v2/projects/<{id}>          | User deletes a project                | 