from flask_testing import TestCase
from manage import app
from flask import current_app
from app.main.config import basedir
import os

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object("app.main.config.DevelopmentConfig")
        return app
        
    def test_development_config(self):
        self.assertTrue(app.config['DEBUG'])
        self.assertFalse(current_app is None)
        self.assertFalse(app.config['SQLALCHEMY_TRACK_MODIFICATIONS'])
        path = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
        self.assertEqual(app.config["SQLALCHEMY_DATABASE_URI"], path)


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object("app.main.config.TestingConfig")
        return app
        
    def test_app_is_testing(self):
        self.assertTrue(app.config['DEBUG'])
        self.assertFalse(app.config['SQLALCHEMY_TRACK_MODIFICATIONS'])
        self.assertFalse(app.config["PRESERVE_CONTEXT_ON_EXCEPTION"])
        path = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
        self.assertEqual(app.config["SQLALCHEMY_DATABASE_URI"], path)

class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)

