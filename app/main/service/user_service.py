from app.main import db
from app.main.model.user import User
import datetime
import pdb;
import uuid

def save_new_user(user):
    usr = User.query.filter_by(email_on=user['email']).first() 
    response = dict(status=None, message=None, code=None)
    
    if not usr:
        new_usr = User(
            email_on = user['email'],
            registered_on = datetime.datetime.utcnow(),
            user_name = user['username'],
            public_id = str(uuid.uuid4()),
            password_hash = user['password']
  
        )
        save_changes(new_usr)
        response['status'] ="success"
        response['message'] = "successfully registered"
        response['code'] = 201
    else:
        response['status'] = "fail"
        response['message'] = "User already exist, Please Log in"
        response['code'] = 409
    return response

def get_all_users():
    return db.session.query(User).all()

def get_a_user(public_id):
    return db.session.query(User).filter_by(public_id=public_id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()