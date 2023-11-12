from app import db, app
import json

@app.route('/api/cardsCatalog', methods=['GET'])
def cardsCatalog():

    query = """SELECT * FROM cardsCatalog"""

    result = {}

    try:
        result = db.read(query)
        status_code = 200
    except Exception as err:
        result = err
        status_code = 400 # The request could not be understood by the server due to incorrect syntax

    response = app.response_class(response=json.dumps(result),
                                status=status_code,
                                mimetype='application/json')

    return response