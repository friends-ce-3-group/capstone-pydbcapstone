from app import db, app
from flask import request
from cors import cors_preflight_response, cors_response
import json
import statuscodes
import tablenames
from scheduledEvents import create_cloudwatch_event_rule, utc_cron_generator
from datetime import datetime, timedelta
from getCard import getCardData

@app.route('/api/testEventBridge', methods=['GET'])
def sendCard():

    cardId = str(request.args.get('cardId'))

    status_code = 500

    # data = sendCardImpl(cardId, app)

    try:

        lambda_function_arn = app.config["LAMBDAARN"]
        role_arn = app.config["EVENTBRIDGEIAMROLEARN"]
        access_key_id = app.config["ACCESS_KEY_ID"]
        access_key = app.config["ACCESS_KEY"]

        now = datetime.now() + timedelta(seconds=30)

        key = "420e9f81-a1e7-4cb0-a945-a9208104ad5c"

        datetime_to_send = utc_cron_generator(now)

        schedule_name = "friends-capstone-send-cards-{}".format(key)

        payload = '{"hey": "cm"}'

        data = create_cloudwatch_event_rule(schedule_name, datetime_to_send, role_arn, lambda_function_arn, payload, access_key_id, access_key)
        
        status_code = statuscodes.STATUS_OK

    except Exception as err:
        data = {"Error" : str(err)}
        status_code = statuscodes.STATUS_ERR

    response = app.response_class(response=json.dumps(data),
                                status=status_code,
                                mimetype='application/json')

    return response

def sendCardImpl(cardId, app):
    lambda_function_arn = app.config["LAMBDAARN"]
    role_arn = app.config["EVENTBRIDGEIAMROLEARN"]
    access_key_id = app.config["ACCESS_KEY_ID"]
    access_key = app.config["ACCESS_KEY"]

    cardData = getCardData(cardId)

    payload = {}
    payload["recipientName"] = cardData["recipientName"]
    payload["recipientEmail"] = cardData["recipientEmail"]
    payload["imagePath"] = cardData["imagePath"]

    sendDate = cardData["sendDate"]
    sendTime = cardData["sendTime"]
    sendDateTime = "{} {}".format(sendDate, sendTime)
    sendDateTime = datetime.datetime.strptime(sendDateTime, "%Y-%m-%d %H:%M:%S")

    schedule_name = "{}-{}-{}".format(payload["recipientName"], payload["recipientEmail"], sendDateTime.strftime("%m/%d/%Y-%H:%M:%S").replace("/","-").replace(":","-"))

    data = create_cloudwatch_event_rule(schedule_name, sendDateTime, role_arn, lambda_function_arn, payload, access_key_id, access_key)

    return data