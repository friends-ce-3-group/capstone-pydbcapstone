import boto3
from dateutil import tz
from datetime import datetime


def create_cloudwatch_event_rule(rule_name, cron_expression, role_arn, lambda_function_arn, payload_json, ACCESS_KEY_ID, ACCESS_KEY):
    
    client = boto3.client('scheduler', region_name="us-east-1", aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=ACCESS_KEY)
    
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

    return response

def utc_cron_generator(sg_date_time):
    from_zone = tz.gettz('Singapore')
    to_zone = tz.gettz('UTC')
    sg_date_time.replace(tzinfo=from_zone)
    utc = sg_date_time.astimezone(to_zone)

    min = utc.minute
    hr = utc.hour
    day_of_month = utc.day
    month = utc.month
    day_of_week = "?"
    year = utc.year

    cron_expression = "cron({} {} {} {} {} {})".format(min, hr, day_of_month, month, day_of_week, year)
    return cron_expression
