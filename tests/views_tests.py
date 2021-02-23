from unittest.mock import patch

from eta_notifications_flask.models import Order
from eta_notifications_flask import db, app

from .base import BaseTest


class ViewsTests(BaseTest):
    def test_get_to_root_should_render_order_list(self):
        order1 = Order(customer_name='Vincent Vega', customer_phone_number='+15551234321')
        order2 = Order(customer_name='Mia Wallace', customer_phone_number='+15551239483')

        db.session.add(order1)
        db.session.add(order2)
        db.session.commit()

        response = self.test_client.get('/orders')
        assert "Vincent Vega" in str(response.data)
        assert "Mia Wallace" in str(response.data)

    def test_send_pickup_notification(self):
        order = Order(customer_name='Vincent Vega', customer_phone_number='+15551234321')

        db.session.add(order)
        db.session.commit()

        self.assertEquals('Ready', order.status)
        self.assertEquals('None', order.notification_status)

        with patch(
            'twilio.rest.api.v2010.account.message.MessageList.create'
        ) as create_mock:
            response = self.test_client.post("/order/{0}/pickup".format(order.id))
            self.assertEquals(response.status_code, 302)
            create_mock.assert_called_once_with(
                body='Your laundry is done and on its way to you!',
                from_=app.config['TWILIO_NUMBER'],
                status_callback=u'http://localhost/order/1/notification/status/update',
                to=u'+15551234321',
            )
            self.assertEquals('Shipped', order.status)
            self.assertEquals('queued', order.notification_status)

    def test_send_deliver_notification(self):
        order = Order(customer_name='Vincent Vega', customer_phone_number='+15551234321')

        db.session.add(order)
        db.session.commit()

        self.assertEquals('Ready', order.status)
        self.assertEquals('None', order.notification_status)

        with patch(
            'twilio.rest.api.v2010.account.message.MessageList.create'
        ) as create_mock:
            response = self.test_client.post("/order/{0}/deliver".format(order.id))
            self.assertEquals(response.status_code, 302)
            create_mock.assert_called_once_with(
                body='Your laundry is arriving now.',
                from_=app.config['TWILIO_NUMBER'],
                status_callback=u'http://localhost/order/1/notification/status/update',
                to=u'+15551234321',
            )
            self.assertEquals('Delivered', order.status)
            self.assertEquals('queued', order.notification_status)

    def test_change_notification_status(self):
        order = Order(customer_name='Vincent Vega', customer_phone_number='+15551234321')

        db.session.add(order)
        db.session.commit()

        self.assertEquals('Ready', order.status)
        self.assertEquals('None', order.notification_status)

        self.test_client.post(
            "/order/{0}/notification/status/update".format(order.id),
            data=dict(
                MessageStatus='sent',
            ),
        )
        self.assertEquals('sent', order.notification_status)
