from app import db, app
import json
import statuscodes
import tablenames

@app.route('/api/cardsCatalog', methods=['GET'])
def cardsCatalog():
    CONST_TABLENAME = tablenames.CARDS_CATALOG_TABLE

    query = "SELECT * FROM {}".format(CONST_TABLENAME)

    data = {}
    status_code = statuscodes.STATUS_ERR
    
    try:
        data = db.read(query)

        status_code = statuscodes.STATUS_OK

    except Exception as err:
        data = { "Error": str(err) }


    response = app.response_class(response=json.dumps(data),
                                status=status_code,
                                mimetype='application/json')

    return response