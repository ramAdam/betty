from app.main.model import User
import datetime

class TestUserModel(BaseTestCase):
    def test_encode_token(self):
        user = User(
            email_on="test@test.ca",
            registered_on = datetime.datetime.utcnow(),
        )
        db.session.add(user)
        

    def test_decode_token(self):
        pass