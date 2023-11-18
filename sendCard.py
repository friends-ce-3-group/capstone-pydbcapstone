from app import app
from flask import request
from cors import cors_preflight_response, cors_response
import json
import statuscodes
import tablenames
from scheduledEvents import create_cloudwatch_event_rule, utc_cron_generator
from datetime import datetime, timedelta
from getCard import getCardData

@app.route('/api/sendCard', methods=['GET'])
def sendCard():

    cardId = str(request.args.get('cardId'))

    data, status_code = sendCardImpl(cardId, app)

    response = app.response_class(response=json.dumps(data),
                                status=status_code,
                                mimetype='application/json')

    return response

def sendCardImpl(cardId, app):
    lambda_function_arn = app.config["LAMBDAARN"]
    role_arn = app.config["EVENTBRIDGEIAMROLEARN"]
    access_key_id = app.config["ACCESS_KEY_ID"]
    access_key = app.config["ACCESS_KEY"]

    data = {}
    cardData, status_code = getCardData(cardId)

    if status_code == statuscodes.STATUS_OK:

        print("\n\n\n",cardData,"\n\n\n")

        payload = {}
        payload["recipientName"] = cardData["recipientName"]
        payload["recipientEmail"] = cardData["recipientEmail"]
        payload["imagePath"] = cardData["imagePath"]
        
        sendDate = cardData["sendDate"]
        sendTime = cardData["sendTime"]
        sendDateTime = "{} {}".format(sendDate, sendTime)
        sendDateTime = datetime.strptime(sendDateTime, "%Y-%m-%d %H:%M:%S")
        datetime_to_send = utc_cron_generator(sendDateTime)

        schedule_name = "{0}-{1}-{2}".format(payload["recipientName"], payload["recipientEmail"].replace("@","."), sendDateTime.strftime("%m/%d/%Y-%H:%M:%S").replace("/","-").replace(":","-"))

        payload_json = json.dumps(payload)

        data = create_cloudwatch_event_rule(schedule_name, datetime_to_send, role_arn, lambda_function_arn, payload_json, access_key_id, access_key)

    return data, status_code




    # try:

    #     lambda_function_arn = app.config["LAMBDAARN"]
    #     role_arn = app.config["EVENTBRIDGEIAMROLEARN"]
    #     access_key_id = app.config["ACCESS_KEY_ID"]
    #     access_key = app.config["ACCESS_KEY"]

    #     now = datetime.now() + timedelta(seconds=30)

    #     key = "420e9f81-a1e7-4cb0-a945-a9208104ad5c"

    #     datetime_to_send = utc_cron_generator(now)

    #     schedule_name = "friends-capstone-send-cards-{}".format(key)

    #     payload = '{"hey": "cm"}'

    #     data = create_cloudwatch_event_rule(schedule_name, datetime_to_send, role_arn, lambda_function_arn, payload, access_key_id, access_key)
        
    #     status_code = statuscodes.STATUS_OK

    # except Exception as err:
    #     data = {"Error" : str(err)}
    #     status_code = statuscodes.STATUS_ERR