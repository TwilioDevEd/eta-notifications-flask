# ETA Notifications for Python - Flask
[![Build Status](https://travis-ci.org/TwilioDevEd/eta-notifications-flask.svg?branch=master)](https://travis-ci.org/TwilioDevEd/eta-notifications-flask)

ETA notifications implementation with Python - Flask and Twilio.

## Local development

This project is built using the [Flask](http://flask.pocoo.org/) web framework. It runs on Python 2.7+ and Python 3.4+.

To run the app locally, first clone this repository and `cd` into its directory. Then:

1. Create a new virtual environment:
    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

        ```
        virtualenv venv
        source venv/bin/activate
        ```

    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

        ```
        mkvirtualenv eta-notifications
        ```

1. Install the requirements:

    ```
    pip install -r requirements.txt
    ```

1. Copy the `.env.example` file to `.env`, and edit it to include your credentials
   for the Twilio API (found at https://www.twilio.com/user/account/settings). You
   will also need a [Twilio Number](https://www.twilio.com/user/account/phone-numbers/incoming).
1. Run `source .env` to apply the environment variables (or even better, use [autoenv](https://github.com/kennethreitz/autoenv))

1. Run the migrations with:

    ```
    python manage.py db upgrade
    ```

1. Seed the database:

   ```
   python manage.py dbseed
   ```

   We have provided an example name and phone number in the seed data. In order for
   the application to send sms notifications, you must edit this seed data providing
   a real phone number where you want to receive the sms notifications. You can edit the
   seed data at `project_root/manage.py`.

1. Start the development server:

    ```
    python manage.py runserver
    ```

You can now access the application at [http://localhost:5000](http://localhost:5000).

## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

1. Run the tests:

    ```
    $ coverage run manage.py test
    ```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.
