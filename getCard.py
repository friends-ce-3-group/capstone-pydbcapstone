
from app import db, app
from flask import request
import json

@app.route('/api/getCard', methods=['GET']) # Flask returns status code 405: The method is not allowed if method is not GET
def getCard():
    CONST_TABLENAME = "Cards"

    cardId = str(request.args.get('cardId'))

    query = "SELECT * FROM {0} WHERE id = {1}".format(CONST_TABLENAME, cardId)

    data = {}
    status_code = 500

    try:
        result = db.read(query)
        if result:
            if len(result) == 1: 
                # single entry found, which is what we expect

                status_code = 200 

                columns = db.get_table_columns(CONST_TABLENAME)
    
                for col, entry in zip(columns, result[0]):
                    key_name = col[0]
                    data[key_name] = entry
            
            else: 
                # more than one entry found. how to deal with this?
                raise ValueError('More than one entry found for the given cardId {}.'.format(cardId))
            
        else:
            # query returns nothing
            raise ValueError('No entry found for cardId {}.'.format(cardId))
        
    except Exception as err:
        data = { "Error": err } # something is wrong with the query, either it returns nothing or it returns more than one entry



    response = app.response_class(response=json.dumps(data),
                                status=status_code,
                                mimetype='application/json')
    
    return response