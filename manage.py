import sys
import unittest

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from eta_notifications_flask.models import Order

from eta_notifications_flask import app, db, config_env_files

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    app.config.from_object(config_env_files['testing'])

    tests = unittest.TestLoader().discover('.', pattern="*_tests.py")
    test_result = unittest.TextTestRunner(verbosity=2).run(tests)

    if not test_result.wasSuccessful():
        sys.exit(1)


@manager.command
def dbseed():
    order1 = Order(customer_name='Vincent Vega', customer_phone_number='+15551234321')
    order2 = Order(customer_name='Mia Wallace', customer_phone_number='+15551239483')

    db.session.add(order1)
    db.session.add(order2)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
