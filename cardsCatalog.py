from app import app, dbConnector as db
import json
# from DBConnect import dbConnector


@app.route('/api/cardsCatalog', methods=['GET'])
def cardsCatalog():

    query = """SELECT * FROM cardsCatalog"""

    result = db.read(query)

    response = app.response_class(response=json.dumps(result),
                                status=200,
                                mimetype='application/json')

    return response
