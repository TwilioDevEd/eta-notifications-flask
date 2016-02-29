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

1. Copy the `.env.example` file to `.env`, and edit it including your credentials
   for the Twilio API (found at https://www.twilio.com/user/account/settings). You
   will also need a [Twilio Number](https://www.twilio.com/user/account/phone-numbers/incoming).
1. Run `source .env` to apply the environment variables (or even better, use [autoenv](https://github.com/kennethreitz/autoenv))

1. Run the migrations with:

    ```
    python manage.py db upgrade
    ```

1. Modify seed data:

   We have provided an example of name and phone number in the seed data. In order for
   the application to send sms notifications, you must edit this seed data providing
   a real phone number where you want the sms notifications to be received.

   In order to do this, you must modify
   [this file](https://github.com/TwilioDevEd/eta-notifications-laravel/blob/master/database/seeds/OrdersTableSeeder.php)
   that is located at: `project_root/manage.py`

1. Seed the database:

   ```
   python manage.py dbseed
   ```

1. Expose your application to the wider internet using ngrok. You can click
   [here](#expose-the-application-to-the-wider-internet) for more details. This step
   is important because the application won't work as expected if you run it through
   localhost.

   ```bash
   $ ngrok http 5000
   ```

1. Start the development server:

    ```
    python manage.py runserver
    ```

    Now you can access the application at your ngrok subdomain that should look
    something like this: `http://<subdomain>.ngrok.io`

### Expose the Application to the Wider Internet

If you want your application to be accessible from the internet, you can either
forward the necessary ports in your router, or use a tool like
[ngrok](https://ngrok.com/) that will expose your local host to the internet.

You can read [this blog](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html)
for more details on how to use ngrok, but if you are using version 2.x, exposing
a specific port it should be easily done with the following command:

```bash
$ ngrok http 5000
```

## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

1. Run the tests:

    ```
    $ coverage run manage.py test
    ```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.
