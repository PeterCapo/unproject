from datetime import datetime
from flask import current_app
from werkzeug.security import generate_password_hash
from app.db_con import connection


projects = []


class Project():
    def __init__(self, project_id=None):
        self.curr = connection().cursor()
        self.project_id = project_id

    def save(self, project_id, projectName, duration, budget, status):

        payload = {
            "Project Name": projectName,
            "budget": budget,
            "duration": duration,
            "status": status
        }
        query = """INSERT INTO projects (projectname, budget, duration, status) VALUES
                (%(Project Name)s, %(budget)s, %(duration)s, %(status)s)"""
        self.curr.execute(query, payload)
        return payload

    def getprojects(self):
        self.curr.execute(
            """SELECT project_id,
            projectName, budget, duration, status FROM projects""")
        data = self.curr.fetchall()
        resp = []

        for projects in data:
            project_id, projectName, budget, duration, status = projects
            datar = dict(
                project_id=int(project_id),
                projectName=projectName,
                duration=int(duration),
                budget=int(budget),
                status=status
            )
            resp.append(datar)

        return resp

    def get_one_project(self, project_id):
        self.curr.execute(
            """SELECT * FROM projects where project_id = %s""", (project_id,))
        data = self.curr.fetchone()
        resp = []

        project_id, projectName, status, budget, duration = data
        project_return = dict(
            project_id=int(project_id),
            projectName=projectName,
            duration=int(duration),
            budget=int(budget),
            status=status
           )
        resp.append(project_return)

        return resp

    def get_one_status(self, status):
        self.curr.execute(
            """SELECT * FROM projects where status = %s""", (status,))
        data = self.curr.fetchall()
        resp = []

        for projects in data:
            project_id, projectName, status, budget, duration = projects
        project_return = dict(
            project_id=int(project_id),
            projectName=projectName,
            duration=int(duration),
            budget=int(budget),
            status=status
           )
        resp.append(project_return)

        return resp

    def update_project(
            self, projectName, status, budget, duration, project_id):
        payload = {
            "Project Name": projectName,
            "status": status,
            "budget": budget,
            "duration": duration
        }
        query = """
        UPDATE projects set projectName =%s, status =%s, budget=%s,
        duration= %s where project_id = %s """
        self.curr.execute(
            query,  (projectName, status, budget, duration, project_id))
        return payload

    def delete(self, project_id):
        """ delete project item """
        self.curr.execute(
            """DELETE FROM projects WHERE project_id = %s""", (project_id,))
        return project_id
