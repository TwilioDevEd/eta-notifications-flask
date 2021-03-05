from eta_notifications_flask.config import config_env_files
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
env = app.config.get("ENV", "production")
app.config.from_object(config_env_files[env])

db = SQLAlchemy()
db.init_app(app)

import eta_notifications_flask.views  # noqa #F401
