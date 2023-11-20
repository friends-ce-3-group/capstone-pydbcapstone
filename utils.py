import boto3
from dateutil import tz
from pytz import timezone
from datetime import datetime
import statuscodes
import json

def create_cloudwatch_event_rule(rule_name, cron_expression, role_arn, lambda_function_arn, payload_json, ACCESS_KEY_ID, ACCESS_KEY):
    
    client = boto3.client('scheduler', region_name="us-east-1", aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=ACCESS_KEY)
    
    status_code = statuscodes.STATUS_ERR

    try:
        response = client.create_schedule(
            Name = rule_name,
            ActionAfterCompletion="DELETE",
            FlexibleTimeWindow={
                'Mode':'OFF' # OFF | FLEXIBLE
            },
            ScheduleExpression=cron_expression,
            # ScheduleExpressionTimezone="Europe/Paris",
            State='ENABLED',
            Target={
                'RoleArn': role_arn,
                'Arn': lambda_function_arn,
                'Input' : payload_json
            }
        )

        status_code = statuscodes.STATUS_OK

    except Exception as err:
        response = { "Error" : str(err) }

    return response, status_code

def utc_cron_generator(sg_date_time):
    # format = "%Y-%m-%d %H:%M:%S"

    # origin = datetime.strptime(sg_date_time, format)

    # origin = origin.replace(tzinfo=timezone(from_timezone))

    utc = sg_date_time.astimezone(timezone("Europe/London"))

    min = utc.minute
    hr = utc.hour
    day_of_month = utc.day
    month = utc.month
    day_of_week = "?"
    year = utc.year

    cron_expression = "cron({} {} {} {} {} {})".format(min, hr, day_of_month, month, day_of_week, year)
    return cron_expression


# def utc_cron_generator(sg_date_time, from_timezone):
#     from_zone = tz.gettz(from_timezone)
#     to_zone = tz.gettz('UTC')
#     sg_date_time.replace(tzinfo=from_zone)
#     utc = sg_date_time.astimezone(to_zone)

#     min = utc.minute
#     hr = utc.hour
#     day_of_month = utc.day
#     month = utc.month
#     day_of_week = "?"
#     year = utc.year

#     cron_expression = "cron({} {} {} {} {} {})".format(min, hr, day_of_month, month, day_of_week, year)
#     return cron_expression


def get_full_datetimestr(sendDate, sendTime, tzone):
    sendDateTime = "{} {}".format(sendDate, sendTime)
    sendDateTime = datetime.strptime(sendDateTime, "%Y-%m-%d %H:%M:%S")
    sendDateTime = sendDateTime.replace(tzinfo=timezone(tzone))
    return sendDateTime



def sendCardImpl(recipientName, recipientEmail, imagePath, sendDate, sendTime, sendTimezone, config):
    lambda_function_arn = config["LAMBDAARN"]
    role_arn = config["EVENTBRIDGEIAMROLEARN"]
    access_key_id = config["ACCESS_KEY_ID"]
    access_key = config["ACCESS_KEY"]

    data = {}
    status_code = statuscodes.STATUS_ERR

    payload = {}
    payload["recipientName"] = recipientName
    payload["recipientEmail"] = recipientEmail
    payload["imagePath"] = imagePath
    
    datetimestr = get_full_datetimestr(sendDate, sendTime, sendTimezone)
    datetimecron = utc_cron_generator(datetimestr)

    schedule_name = "{0}-{1}-{2}".format(payload["recipientName"], payload["recipientEmail"].replace("@","."), datetimestr.strftime("%m/%d/%Y-%H:%M:%S").replace("/","-").replace(":","-"))

    payload_json = json.dumps(payload)

    data, status_code = create_cloudwatch_event_rule(schedule_name, datetimecron, role_arn, lambda_function_arn, payload_json, access_key_id, access_key)

    data["cron expr"] = datetimecron
    data["send_Date"] = str(sendDate)
    data['send_Time'] = str(sendTime)

    return data, status_code