from eta_notifications_flask import app, db
from flask import flash, redirect, render_template, request

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

@app.route('/order/<order_id>/pickup')
def order_pickup(order_id):
    order = Order.query.get(order_id)

    return render_template('show.html', order=order)

@app.route('/order/<order_id>/deliver')
def order_deliver(order_id):
    order = Order.query.get(order_id)

    return render_template('show.html', order=order)
