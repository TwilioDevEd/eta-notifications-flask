import unittest
from eta_notifications_flask.models import Order


class BaseTest(unittest.TestCase):
    def setUp(self):
        from eta_notifications_flask import app, db
        self.app = app
        self.db = db
        self.test_client = app.test_client()
        self.app.config['WTF_CSRF_ENABLED'] = False

    def tearDown(self):
        Order.query.delete()
        self.db.session.commit()
