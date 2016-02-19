from eta_notifications_flask.models import app_db

db = app_db()

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String, nullable=False)
    customer_phone_number = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    notification_status = db.Column(db.String, nullable=False)

    def __init__(self, customer_name, customer_phone_number):
        self.customer_name = customer_name
        self.customer_phone_number = customer_phone_number

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    # Python 3

    def __unicode__(self):
        return self.id

    def __repr__(self):
        return '<Order %r>' % (self.id)
