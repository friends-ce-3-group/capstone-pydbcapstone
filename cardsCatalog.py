import json
from app import app

@app.route('/api/cardsCatalog', methods=['GET'])
def cardsCatalog():

    from DBConnect import db_read

    query = """SELECT * FROM cardsCatalog"""

    result = db_read(query)

    response = app.response_class(response=json.dumps(result),
                                status=200,
                                mimetype='application/json')

    return response
