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

# @app.route('/api/testConfig', methods=['GET'])
# def testConfig():
#     data = {}
#     data["ENDPOINT"] = app.config["ENDPOINT"]
#     data["DBUSER"] = app.config["DBUSER"]
#     data["DBPASS"] = app.config["DBPASS"]

#     response = app.response_class(response=json.dumps(data),
#                                   status=200,
#                                   mimetype='application/json')
    
#     return response

@app.route('/api/getCardsTable', methods=['GET'])
def createTable():

    connection = mysql.connector.connect(
        host=app.config["ENDPOINT"],
        user=app.config["DBUSER"],
        password=app.config["DBPASS"],
        database=app.config["DBNAME"]
    )

    cursor = connection.cursor()

    query = """SELECT * FROM Cards"""

    cursor.execute(query)

    result = cursor.fetchall()

    response = app.response_class(response=json.dumps(result),
                                status=200,
                                mimetype='application/json')

    return response