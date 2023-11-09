from app import app
import json
import getEndPoint
import mysql.connector

@app.route('/api/testdb', methods=['GET'])
def testdb():
    data = getEndPoint.get_rds_endpoint()

    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    
    return response


@app.route('/api/createTable', methods=['GET'])
def createTable():
    data = getEndPoint.get_rds_endpoint()

    endpoint = data["endpoint"]

    connection = mysql.connector.connect(
        host=endpoint,
        user="admin",
        password="password",
    )

    cursor = connection.cursor()

    cursor.execute("CREATE TABLE CardsTemp (id VARCHAR(255), imageKey VARCHAR(255), imageCategory VARCHAR(255))")
    result = cursor.fetchall()

    connection.close()

    response = app.response_class(response=json.dumps(result),
                                status=200,
                                mimetype='application/json')

    return response