# ETA Notifications for Python - Flask
![Flask](https://github.com/TwilioDevEd/eta-nofitifcations-flask/workflows/Flask/badge.svg)

ETA notifications implementation with Python - Flask and Twilio.

## Local development

This project is built using the [Flask](http://flask.pocoo.org/) web framework. It runs on Python 2.7+ and Python 3.4+.

To run the app locally, first clone this repository and `cd` into its directory. Then:

1. Create and activate a new python3 virtual environment.

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

1. Install the requirements:

    ```bash
    pip install -r requirements.txt
    ```

1. Copy the sample configuration file and edit it to match your configuration.

   ```bash
   cp .env.example .env
   ```

   Twilio API credentials can be found [here](https://www.twilio.com/console) 
   and find you can create a REST API Key [here](https://www.twilio.com/console/project/api-keys).
   If using the twilio CLI you can run:
   
   ```bash
   twilio api:core:keys:create --friendly-name=worm-transfer -o json
   ```
   
   Copy or create a Twilio phone number from [here](https://www.twilio.com/console/phone-numbers).

1. Run the migrations with:

    ```bash
    python manage.py db upgrade
    ```

1. Modify seed data:

   We have provided an example of name and phone number in the seed data. In order for
   the application to send sms notifications, you must edit this seed data providing
   a real phone number where you want the sms notifications to be received.

   In order to do this, you must modify
   [this file](https://github.com/TwilioDevEd/eta-notifications-flask/blob/master/manage.py#L23)
   that is located at: `project_root/manage.py`

1. Seed the database:

   ```bash
   python manage.py dbseed
   ```

1. Expose your application to the wider internet using ngrok. You can click
   [here](#expose-the-application-to-the-wider-internet) for more details. This step
   is important because the application won't work as expected if you run it through
   localhost.

   ```bash
   ngrok http 5000
   ```

1. Start the development server:

    ```bash
    python manage.py runserver
    ```

Once Ngrok is running, open up your browser and go to your Ngrok URL. It will
look like this: `http://9a159ccf.ngrok.io`

That's it!

### Expose the Application to the Wider Internet

If you want your application to be accessible from the internet, you can either
forward the necessary ports in your router, or use a tool like
[ngrok](https://ngrok.com/) that will expose your local host to the internet.

You can read [this blog post](https://www.twilio.com/blog/2015/09/6-awesome-reasons-to-use-ngrok-when-testing-webhooks.html)
for more details on how to use ngrok, but if you are using version 2.x, exposing
a specific port should be easily done with the following command:

```bash
ngrok http 5000
```

## Run the tests

```bash
python manage.py test
```

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](LICENSE)
* Lovingly crafted by Twilio Developer Education.