from app import db, app
from flask import request
from cors import cors_preflight_response, cors_response
import json
import statuscodes
import tablenames

@app.route('/api/getCard', methods=['GET','OPTIONS']) # Flask returns status code 405: The method is not allowed if method is not GET
def getCard():
    if request.method == "OPTIONS":

        return cors_preflight_response()

    else:
        CONST_TABLENAME = tablenames.CARDS_TABLE

        cardId = str(request.args.get('cardId'))

        query = "SELECT * FROM {0} WHERE id = {1}".format(CONST_TABLENAME, cardId)

        data = {}
        status_code = statuscodes.STATUS_ERR

        try:
            data, status_code = db.processed_read_data(CONST_TABLENAME, query)

            if status_code == statuscodes.STATUS_ERR:
                raise ValueError('No entry found for cardId {}.'.format(cardId))
            
        except Exception as err:
            data = { "Error": str(err) } # something went wrong with the query



        response = app.response_class(response=json.dumps(data),
                                    status=status_code,
                                    mimetype='application/json')
        
        return cors_response(response)