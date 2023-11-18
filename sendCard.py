from endpoint_includes import *
from scheduledEvents import create_cloudwatch_event_rule, utc_cron_generator
from datetime import datetime
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