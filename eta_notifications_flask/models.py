from eta_notifications_flask import db

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String, nullable=False)
    customer_phone_number = db.Column(db.String, nullable=False)
    status = db.Column(db.Enum('Ready', 'Shipped', 'Delivered', name='status_enum'),
                       nullable=False, default='Ready')
    notification_status = db.Column(db.Enum('None', 'queued', 'sent', 'delivered',
                                            'undelivered', 'failed', name='notification_status_enum'),
                                    nullable=False, default='None')

    def __init__(self, customer_name, customer_phone_number, status='Ready', notification_status='None'):
        self.customer_name = customer_name
        self.customer_phone_number = customer_phone_number
        self.status = status
        self.notification_status = notification_status

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
