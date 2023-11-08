from app import app
import json
import boto3

@app.route('/api/testdb', methods=['GET'])
def testdb():
    region = 'us-west-2'
    db_instance = 'terraform-20231108025942138300000001'

    source = boto3.client('rds', region_name=region)

    data = {}

    try:
        instances = source.describe_db_instances(DBInstanceIdentifier=db_instance)
        rds_host = instances.get('DBInstances')[0].get('Endpoint').get('Address')
        rds_port = instances.get('DBInstances')[0].get('Endpoint').get('Port')

        data = { "Address" : rds_host, "Port" : rds_port }
    except BaseException as e:
        data = { "Error" : str(e) }

    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    
    return response