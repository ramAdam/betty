from ..util.dto import UserDto
from flask_restplus import Resource
from ..service.user_service import get_all_users, save_new_user, get_a_user
from flask import request
import pdb

api = UserDto.api
_user = UserDto.user
_usrlst = UserDto.userlst

@api.route('/')
class UserList(Resource):
    @api.doc("List all registered user")
    @api.marshal_list_with(_usrlst, envelope='data')
    def get(self):
        """list of all registered user"""
        return get_all_users()

    @api.doc("create a new user")
    @api.response(201, "user successfully created")
    @api.expect(_user, validate=True)
    def post(self):
        """create a new user"""
        data = request.json
        return save_new_user(data)
        

@api.route('/<public_id>')
@api.param('public_id', "The user identifier")
@api.response(404, "User not found")
class User(Resource):
    @api.doc("get a user")
    @api.marshal_list_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user =  get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
    
    