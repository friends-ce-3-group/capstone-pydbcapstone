from app import app
import json
# from DBConnect import dbConnector


@app.route('/api/cardsCatalog', methods=['GET'])
def cardsCatalog():

    query = """SELECT * FROM cardsCatalog"""

    # result = dbConnector.read(query)

    # response = app.response_class(response=json.dumps(result),
    #                             status=200,
    #                             mimetype='application/json')

    import mysql.connector

    connection = mysql.connector.connect(
        host=app.config["ENDPOINT"],
        user=app.config["DBUSER"],
        password=app.config["DBPASS"],
        database=app.config["DBNAME"]
    )
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    response = app.response_class(response=json.dumps(result),
                                status=200,
                                mimetype='application/json')

    return response
