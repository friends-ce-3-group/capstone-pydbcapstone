from app import app
import json
from DBConnect import dbConnector

@app.route('/api/getCardsTable', methods=['GET'])
def createTable():

    query = """SELECT * FROM Cards"""

    result = dbConnector.execute(query)

    response = app.response_class(response=json.dumps(result),
                                status=200,
                                mimetype='application/json')

    return response