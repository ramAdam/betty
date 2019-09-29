from app.main import db
from app.main.model.blacklist import BlackListToken

def save(token):
    response_object = dict(status=None, message=None)
    try:
        b_token = BlackListToken(token)
        db.session.add(b_token)
        db.commit()
        response["status"] = "success"
        response["message"] = "token successfully saved"

    except Exception as e:
        response["status"] = "failed"
        response["message"] = e

    return response_object, 200
        