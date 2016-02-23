from eta_notifications_flask import app, db
from flask import url_for, flash, redirect, render_template, request
from twilio.rest import TwilioRestClient

from eta_notifications_flask.models import Order

@app.route('/')
def order_index():
    orders = Order.query.all()

    return render_template('index.html', orders=orders)

@app.route('/order/<order_id>')
def order_show(order_id):
    order = Order.query.get(order_id)

    return render_template('show.html', order=order)

@app.route('/order/<order_id>/pickup', methods=["POST"])
def order_pickup(order_id):
    order = Order.query.get(order_id)
    order.status = 'Shipped'
    order.notification_status = 'queued'
    db.session.commit()

    callback_url = request.base_url.replace('/pickup', '') + '/notification/status/update'
    send_sms_notification(order.customer_phone_number,
                          'Your clothes will be sent and will be delivered in 20 minutes',
                          callback_url)

    return redirect(url_for('order_show', order_id=order_id))

@app.route('/order/<order_id>/deliver', methods=["POST"])
def order_deliver(order_id):
    order = Order.query.get(order_id)
    order.status = 'Delivered'
    order.notification_status = 'queued'
    db.session.commit()

    callback_url = request.base_url.replace('/deliver', '') + '/notification/status/update'
    send_sms_notification(order.customer_phone_number,
                          'Your clothes have been delivered',
                          callback_url)

    return redirect(url_for('order_index'))

@app.route('/order/<order_id>/notification/status/update', methods=["POST"])
def order_deliver_status(order_id):
    order = Order.query.get(order_id)
    order.notification_status = request.form['MessageStatus']
    db.session.commit()

    return render_template('show.html', order=order)

def send_sms_notification(to, message_body, callback_url):
    account_sid = app.config['TWILIO_ACCOUNT_SID']
    auth_token  = app.config['TWILIO_AUTH_TOKEN']
    twilio_number = app.config['TWILIO_NUMBER']
    client = TwilioRestClient(account_sid, auth_token)
    client.messages.create(to=to,
                           from_=twilio_number,
                           body=message_body,
                           status_callback=callback_url)
