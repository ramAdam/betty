from .. import db, flask_bcrypt
import jwt
import datetime

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email_on = db.Column(db.String, unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    user_name = db.Column(db.String, unique=True)
    public_id = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))

    @property
    def password(self):
        raise AttributeError('password write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)
    
    @staticmethod
    def encode_auth_token(self, user_id):
        """
            Generate auth token and
            returns a string
        """
        try:
            payload ={
                "exp":datetime.now.utcnow() + datetime.timedelta(days=1, seconds=5)
                "iat":datetime.now(),
                "sub":user_id
            }
            return jwt.encode{
                payload,
                key,
                algorithm = "HS256"
            }
        except Exception as e:
            raise e
    
    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwd.decode.token(auth_token)
            is_blacklisted = BlackListToken.check_blacklist(auth_token)
            if is_blacklisted:
                return "Token black listed, please log in again"
            else:
                return payload["sub"]
        except jwt.ExpiredSignatureError:
            return "Signature expired"
        except jwt.InvalidTokenError:
            return "Invalid token, Please log in again"

    def __repr__(self):
        return "<User '{}'>".format(self.user_name)