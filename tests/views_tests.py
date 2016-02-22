import six
from eta_notifications_flask.models.order import Order
from eta_notifications_flask import db, app

if six.PY3:
    from unittest.mock import patch
else:
    from mock import patch

from base import BaseTest

class ViewsTests(BaseTest):
    def test_get_to_root_should_render_order_list(self):
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

        response = self.test_client.get('/')
        assert b"Vincent Vega" in response.data
        assert b"Mia Wallace" in response.data

    def test_send_pickup_notification(self):
        order = Order(
            customer_name='Vincent Vega',
            customer_phone_number='+15551234321'
        )

        db.session.add(order)
        db.session.commit()

        self.assertEquals('Ready', order.status)
        self.assertEquals('None', order.notification_status)

        with patch('twilio.rest.resources.messages.Messages.create') as create_mock:
            response = self.test_client.post("/order/{0}/pickup".format(order.id))
            create_mock.assert_called_once_with(
                body='Your clothes will be sent and will be delivered in 20 minutes',
                from_=app.config['TWILIO_NUMBER'],
                status_callback=u'http://localhost/order/1/pickup/status',
                to=u'+15551234321'
            )
            self.assertEquals('Shipped', order.status)
            self.assertEquals('Queued', order.notification_status)

    def test_send_deliver_notification(self):
        order = Order(
            customer_name='Vincent Vega',
            customer_phone_number='+15551234321'
        )

        db.session.add(order)
        db.session.commit()

        self.assertEquals('Ready', order.status)
        self.assertEquals('None', order.notification_status)

        with patch('twilio.rest.resources.messages.Messages.create') as create_mock:
            response = self.test_client.post("/order/{0}/deliver".format(order.id))
            create_mock.assert_called_once_with(
                body='Your clothes have been delivered',
                from_=app.config['TWILIO_NUMBER'],
                status_callback=u'http://localhost/order/1/deliver/status',
                to=u'+15551234321'
            )
            self.assertEquals('Delivered', order.status)
            self.assertEquals('Queued', order.notification_status)

    def test_change_pickup_status(self):
        order = Order(
            customer_name='Vincent Vega',
            customer_phone_number='+15551234321'
        )

        db.session.add(order)
        db.session.commit()

        self.assertEquals('Ready', order.status)
        self.assertEquals('None', order.notification_status)

        self.test_client.post("/order/{0}/pickup/status".format(order.id), data=dict(
            MessageStatus='Some Status',
        ))
        self.assertEquals('Some Status', order.notification_status)

    def test_change_deliver_status(self):
        order = Order(
            customer_name='Vincent Vega',
            customer_phone_number='+15551234321'
        )

        db.session.add(order)
        db.session.commit()

        self.assertEquals('Ready', order.status)
        self.assertEquals('None', order.notification_status)

        self.test_client.post("/order/{0}/deliver/status".format(order.id), data=dict(
            MessageStatus='Some Status',
        ))
        self.assertEquals('Some Status', order.notification_status)

if __name__ == '__main__':
    unittest.main()
