from eta_notifications_flask import app, db
from flask import url_for, flash, redirect, render_template, request
from twilio.rest import TwilioRestClient

from eta_notifications_flask.models import init_models_module

init_models_module(db, app)

from eta_notifications_flask.models.order import Order

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
    update_order_stauts('Shipped', order)
    update_notification_status('Queued', order)
    send_sms_notification(order.customer_phone_number,
                          'Your clothes will be sent and will be delivered in 20 minutes')

    return redirect(url_for('order_show', order_id=order_id))

@app.route('/order/<order_id>/deliver', methods=["POST"])
def order_deliver(order_id):
    order = Order.query.get(order_id)
    update_order_stauts('Delivered', order)
    update_notification_status('Queued', order)

    send_sms_notification(order.customer_phone_number,
                          'Your clothes have been delivered')

    return redirect(url_for('order_show', order_id=order_id))

@app.route('/order/<order_id>/pickup/status', methods=["POST"])
def order_pickup_status(order_id):
    order = Order.query.get(order_id)
    update_notification_status(request.form['MessageStatus'], order)

    return render_template('show.html', order=order)

@app.route('/order/<order_id>/deliver/status', methods=["POST"])
def order_deliver_status(order_id):
    order = Order.query.get(order_id)
    update_notification_status(request.form['MessageStatus'], order)

    return render_template('show.html', order=order)

def update_order_stauts(status, order):
    order.status = status
    db.session.commit()

def update_notification_status(status, order):
    order.notification_status = status
    db.session.commit()

def send_sms_notification(to, message_body):
    account_sid = app.config['TWILIO_ACCOUNT_SID']
    auth_token  = app.config['TWILIO_AUTH_TOKEN']
    twilio_number = app.config['TWILIO_NUMBER']
    callback_url = request.base_url + '/status'
    client = TwilioRestClient(account_sid, auth_token)
    client.messages.create(to=to,
                           from_=twilio_number,
                           body=message_body,
                           status_callback=callback_url)
