from .. import db
import datetime

class BlackListToken(db.Model):
    __tablename__ = "BlackListToken"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()
    
    def __repr__(self):
        return "Token{}".format(self.token)

    @staticmethod
    def check_blacklist(auth_token):
        res = BlackListToken.query.filter(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False