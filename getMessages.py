from app import db, app
from flask import request
import json

@app.route('/api/getMessages', methods=['GET'])
def getMessages():
    CONST_TABLENAME = "Messages"

    cardId = str(request.args.get('cardId'))

    query = "SELECT * FROM {0} WHERE id = {1}".format(CONST_TABLENAME, cardId)

    data = {}
    status_code = 500

    # print(query)

    try:
        result = db.read(query)
        # print(result)

        if result:
            if len(result) == 1: 

                status_code = 200 

                columns = db.get_table_columns(CONST_TABLENAME)
    
                for col, entry in zip(columns, result[0]):
                    key_name = col[0]
                    data[key_name] = entry
            
            else:
                columns = db.get_table_columns(CONST_TABLENAME)

                for idx, found in enumerate(result):
                    entry_data = {}
                    for col, entry in zip(columns, found):
                        key_name = col[0]
                        entry_data[key_name] = entry

                    data[idx] = entry_data
            
        else:
            # query returns nothing
            raise ValueError('No entry found for cardId {}.'.format(cardId))
        
    except Exception as err:
        data = { "Error": str(err) } # something is wrong with the query, either it returns nothing or it returns more than one entry



    response = app.response_class(response=json.dumps(data),
                                status=status_code,
                                mimetype='application/json')
    
    return response