import boto3

def get_rds_endpoint():
    region = 'us-west-2'
    db_instance = 'terraform-20231109165327493200000001'

    source = boto3.client('rds', region_name=region)

    data = {}

    try:
        instances = source.describe_db_instances(DBInstanceIdentifier=db_instance)
        db_instance = instances['DBInstances'][0]
        endpoint = db_instance['Endpoint']['Address']
        port = db_instance['Endpoint']['Port']

        data = { "endpoint" : endpoint, "port" : port }
    except BaseException as e:
        data = { "Error" : str(e) }

    return data

