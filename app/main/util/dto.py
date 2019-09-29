from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace("user", description="user related operations")
    u_fields = dict(
        email = fields.String(attribute="email_on",required=True, default="fields don't match", description="user email address"),
        username = fields.String(required=True, description="user name"),
        password = fields.String(required=True, description="user password"),
        public_id = fields.String(required=True, description="user identifier")
    )
    user = api.model("user", u_fields)
    userlst = api.model("userlist", dict(id=fields.String(attribute="user_name")))