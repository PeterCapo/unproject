from flask_restful import Resource, reqparse
import json
import datetime
from flask import jsonify, make_response, request
from functools import wraps
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.v2.models.projects import projects, Project
from app.api.v2.models.users import UserModel
from app.api.v2.validators.utils import Validators


def admin_only(_f):
    ''' Restrict access if not admin '''
    @wraps(_f)
    def wrapper_function(*args, **kwargs):
        user = UserModel().get_by_email(get_jwt_identity())

        print(user)

        if not user[3]:
            return {
                'message':
                'No access, you must be an admin to access'
            }, 401
        return _f(*args, **kwargs)
    return wrapper_function


def user_only(_f):
    ''' Restrict access if not attendant '''
    @wraps(_f)
    def wrapper_function(*args, **kwargs):
        user = UserModel().get_by_email(get_jwt_identity())

        if user[3]:
            return {
                'message':
                'Anauthorized access, you must be an attendant to access'}, 401
        return _f(*args, **kwargs)
    return wrapper_function


class SpecificProject(Resource, Project):
    def __init__(self):
        self.ops = Project()

    def get(self, id):
        projects = self.ops.get_one_project(id)
        return make_response(jsonify(
            {
                'Message': 'Specific project',
                'status': 'ok',
                'Data': projects
            }), 200)

    @jwt_required
    @admin_only
    def delete(self, id):
        project = self.ops.delete(id)
        return make_response(jsonify(
                {
                    'Message': 'Deleted',
                    'status': 'ok',
                    'Data': project
                }), 200)


class Specificstatus(Resource, Project):
    def __init__(self):
        self.ops = Project()

    def get(self, status):
        projects = self.ops.get_one_status(status)
        return make_response(jsonify(
            {
                'Message': 'Specific project status',
                'status': 'ok',
                'Data': projects
            }), 200)


class UpdateProject(Resource, Project):
    def __init__(self):
        self.ops = Project()

    @jwt_required
    @admin_only
    def put(self, id):
        data = json.loads(request.data)
        assert(data['Project Name'])
        assert(data['status'])
        assert (data['budget'])
        assert(data['duration'])
        assert (id)

        result = self.ops.update_project(
            data['Project Name'],
            data['status'], data['budget'], data['duration'], id)
        return make_response(jsonify(
                    {
                        'Message': 'Project updated',
                        'status': 'ok',
                        'Data': result
                    }), 200)


class Projects(Resource, Project):
    parser = reqparse.RequestParser()

    parser.add_argument("Project Name", type=str, required=True,
                        help="This field can not be left bank")
    parser.add_argument("status", type=str, required=True,
                        help="This field can not be left bank")
    parser.add_argument("duration", type=int, required=True,
                        help="This field can not be left bank")
    parser.add_argument("budget", type=int, required=True,
                        help="This field can not be left bank")

    def __init__(self):
        self.ops = Project()

    def get(self):
        projects = self.ops.getprojects()
        return make_response(jsonify(
            {
                'Status': "Ok",
                'Message': "Success",
                'All Projects': projects
            }), 200)

    @jwt_required
    @admin_only
    def post(self):
        data = Projects.parser.parse_args()
        id = len(projects) + 1
        projectName = data['Project Name']
        duration = data['duration']
        budget = data['budget']
        status = data['status']

        result = self.ops.save(id, projectName, duration, budget, status)

        if Validators.empty_fields(
            self, projectName, budget, duration, status
        ):
                return {'message':
                        "blank field not allowed"}
        if next(
            filter(
                lambda x:
                x['Project Name'] == projectName, projects), None) is not None:
            return {'message':
                    "A project with name'{}' already exists."
                    .format(projectName)
                    }
        payload = {
            'id': id,
            'Project Name': projectName,
            'budget': budget,
            'duration': duration,
            'status': status

        }
        projects.append(payload)
        return make_response(jsonify(
            {
                'Message': 'Project created',
                'status': 'ok',
                'Data': result
            }), 201)


class SignUp(Resource, UserModel):

    parser = reqparse.RequestParser()

    parser.add_argument("email", type=str, required=True,
                        help="This field can not be left bank")
    parser.add_argument("password", type=str, required=True,
                        help="This field can not be left bank")

    @jwt_required
    @admin_only
    def post(self):
        """ Create a new user"""
        data = SignUp.parser.parse_args()
        email = data["email"]
        password = data["password"]

        validate = Validators()
        if not validate.valid_email(email):
            return {"message": "enter valid email"}, 400
        if not validate.valid_password(password):
            return {
                "message":
                "password should have a capital letter & includes number"
            }, 400
        if UserModel().get_by_email(email):
            return {"message":
                    "user with {} already exists"
                    .format(email)}, 400
        user = UserModel(email, password)
        user.save()
        return {"message": "user {} created successfully".format(email)}, 201


class Login(Resource, UserModel):
    parser = reqparse.RequestParser()

    parser.add_argument("email", type=str, required=True,
                        help="This field can not be left bank")
    parser.add_argument("password", type=str, required=True,
                        help="This field can not be left bank")

    def post(self):
        data = Login.parser.parse_args()
        email = data["email"]
        password = data["password"]
        user = UserModel().get_by_email(email)
        if user and check_password_hash(user[2], password):
            expires = datetime.timedelta(days=2)
            token = create_access_token(user[1], expires_delta=expires)
            return {'token': token, 'message': 'successfully logged'}, 201
        return {'message': 'user not found'}, 404
