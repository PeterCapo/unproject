import time
from flask_restful import abort
import re


class Validators:
    def empty_fields(self, projectName, budget, duration, status):
        if projectName == "" or budget == "":
            if duration == "" or status == "":
                res = 'blank field not allowed'
            return res

    def empty_projects_fields(self, region, country, projectId):
        if region == "" or country == "" or projectId == "":
            res = 'blank field not allowed'
            return res

    def valid_password(self, password):
        """validate for password """
        regex = "^[a-zA-Z0-9_ ]+$"
        return re.match(regex, password)

    def valid_email(self, email):
        """ validate for email """
        return re.match("^[^@]+@[^@]+[^@]+$", email)
