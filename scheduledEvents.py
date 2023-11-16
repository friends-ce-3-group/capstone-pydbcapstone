import boto3

# # Replace these values with your AWS credentials and region
# aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
# aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
# aws_region = 'us-east-1'  # Change to your desired AWS region

# Replace these values with your Lambda function details
# lambda_function_arn = 'arn:aws:lambda:us-east-1:123456789012:function:your-lambda-function'
# rule_name = 'your-cloudwatch-rule'

def create_cloudwatch_event_rule(rule_name, cron_expression, role_arn, lambda_function_arn):
    
    client = boto3.client('scheduler', region_name="us-east-1")
    
    response = client.create_schedule(
        Name = rule_name,
        ActionAfterCompletion="DELETE",
        FlexibleTimeWindow={
            'Mode':'OFF' # OFF | FLEXIBLE
        },
        ScheduleExpression=cron_expression,
        ScheduleExpressionTimezone="Europe/Paris",
        State='ENABLED',
        Target={
            'Arn': lambda_function_arn,
            'RoleArn': role_arn,
            'Input' : '{"hey": "there"}'
        }
    )

    return response

def utc_cron_generator(sg_min, sg_hr, sg_day_of_month, sg_month, sg_day_of_week, sg_year):
    cron_expression = "cron({} {} {} {} {} {})".format(sg_min, sg_hr - 8, sg_day_of_month, sg_month, sg_day_of_week, sg_year)
    return cron_expression
