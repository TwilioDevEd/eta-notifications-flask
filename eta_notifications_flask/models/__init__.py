model_settings = {
    'db': None,
    'app': None,
}


def init_models_module(db, flask_app):
    model_settings['db'] = db
    model_settings['app'] = flask_app


def app_db():
    return model_settings['db']

def auth_token():
    return model_settings['app'].config['TWILIO_AUTH_TOKEN']


def phone_number():
    return model_settings['app'].config['TWILIO_NUMBER']


def account_sid():
    return model_settings['app'].config['TWILIO_ACCOUNT_SID']
