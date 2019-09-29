from flask_script import Manager
from app.main import create_app, db
from flask_migrate import Migrate, MigrateCommand
from app.main.model import user, blacklist
from app import blueprint
import unittest

app = create_app("dev")
app.register_blueprint(blueprint)
app.app_context().push()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    tests = unittest.TestLoader().discover("app/test", pattern="test_*.py")
    results = unittest.TextTestRunner(verbosity=2).run(tests)
    if results.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    manager.run()