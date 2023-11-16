from app import db, app
from flask import request
from cors import cors_preflight_response, cors_response
import json
import statuscodes
import tablenames
from scheduledEvents import create_cloudwatch_event_rule, utc_cron_generator
import datetime

@app.route('/api/testEventBridge', methods=['GET'])
def testEventBridge():

    status_code = 500

    try:

        lambda_function_arn = app.config["LAMBDAARN"]
        role_arn = app.config["EVENTBRIDGEIAMROLEARN"]

        now = datetime.datetime.now()

        min = now.minute + 1
        hr = now.hour
        day_of_month = now.day
        month = now.month
        day_of_week = "?"
        year = now.year

        key = "420e9f81-a1e7-4cb0-a945-a9208104ad5c"

        cron_expression = utc_cron_generator(min, hr, day_of_month, month, day_of_week, year)

        rule_name = "friends-capstone-send-cards-{}".format(key)

        data = create_cloudwatch_event_rule(rule_name, cron_expression, role_arn, lambda_function_arn)
        
        status_code = statuscodes.STATUS_OK

    except Exception as err:
        data = {"Error" : err}
        status_code = statuscodes.STATUS_ERR

    print(data)

    response = app.response_class(response=json.dumps(data),
                                status=status_code,
                                mimetype='application/json')

    return response