from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from eta_notifications_flask.models.order import Order

from eta_notifications_flask import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('.', pattern="*_tests.py")
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def dbseed():
    order1 = Order(
        customer_name='Vincent Vega',
        customer_phone_number='+15551234321'
    )
    order2 = Order(
        customer_name='Mia Wallace',
        customer_phone_number='+15551239483'
    )

    db.session.add(order1)
    db.session.add(order2)
    db.session.commit()

if __name__ == "__main__":
    manager.run()
