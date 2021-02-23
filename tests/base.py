import unittest
from eta_notifications_flask import app, db


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        db.create_all()
        self.test_client = app.test_client()

    def tearDown(self):
        db.drop_all()
