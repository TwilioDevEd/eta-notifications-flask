from eta_notifications_flask import app
from flask import flash, redirect, render_template, request

@app.route('/')
def index():
    return render_template('index.html')
