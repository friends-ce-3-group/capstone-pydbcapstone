from app import db, app
from flask import request
import json

@app.route('/api/signCard', methods=['POST'])
def signCard():
    CONST_TABLENAME = "Messages"

    input = request.get_json()

    id = input['id']
    cardId = input['cardId']
    name = input['name']
    message = input['message']
    wordCount = input['wordCount']
    createdDateTime = input['createdDateTime']

    query = """INSERT INTO {} 
    (id, cardId, name, message, wordCount, createdDateTime) 
    VALUES ('{}', '{}', '{}', '{}', '{}', '{}')""".format(CONST_TABLENAME, 
        id, cardId, name, message, wordCount, createdDateTime)

    data = {}
    status_code = 500

    try:
        result = db.write(query)

        if len(result) == 0:

            status_code = 200 
        
        else: 
            raise ValueError('Unable to sign card.')
            
    except Exception as err:
        data = { "Error": str(err) } # something is wrong with the query, either it returns nothing or it returns more than one entry


    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    
    return response