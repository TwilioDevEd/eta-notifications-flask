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
    orders = Order.query.all()

    return render_template('index.html', orders=orders)
