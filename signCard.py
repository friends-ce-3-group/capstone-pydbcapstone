from app import db, app
from flask import request
from cors import cors_preflight_response, cors_response
import json
import statuscodes
import tablenames

@app.route('/api/signCard', methods=['POST','OPTIONS'])
def signCard():
    if request.method == "OPTIONS":

        return cors_preflight_response()

    else:
        CONST_TABLENAME = tablenames.MESSAGES_TABLE

        input = request.get_json()

        data = {}
        status_code = statuscodes.STATUS_ERR

        try:
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
        
            result = db.write(query)

            if len(result) == 0:

                status_code = statuscodes.STATUS_OK 
            
            else: 
                raise ValueError('Unable to sign card.')
                
        except Exception as err:
            data = { "Error": str(err) } # something is wrong with the query, either it returns nothing or it returns more than one entry


        response = app.response_class(response=json.dumps(data),
                                    status=status_code,
                                    mimetype='application/json')
        
        return cors_response(response)