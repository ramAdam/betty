from flask_restplus import Api
from flask import Blueprint
from .main.controller.user_controller import api as user_ns
# import pdb


blueprint = Blueprint("api", __name__)
# pdb.set_trace()
api = Api(
    blueprint,
    title="FLASK RESTPLUS API BOILERPLATE WITH JWT",
    version = "1.0",
    description = "boilerplate for flask restful service"
)
api.add_namespace(user_ns, "/user")