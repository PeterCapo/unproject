from flask_restful import Api
from flask import Blueprint


from .views import Projects, Login
from .views import SpecificProject, Specificstatus
from .views import UpdateProject, SignUp


version2 = Blueprint('api2', __name__, url_prefix='/api/v2')


api = Api(version2)


api.add_resource(Projects, '/project')
api.add_resource(SpecificProject, '/projects/<int:id>')
api.add_resource(Specificstatus, '/projects/status/<status>')
api.add_resource(UpdateProject, '/projects/<int:id>')
api.add_resource(Login, '/login')
api.add_resource(SignUp, '/signup')
