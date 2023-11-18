from app import app
from flask import request
from DBConnect import DBConnector
from cors import cors_preflight_response, cors_response
import json
import statuscodes
import tablenames

@app.route('/api/createCard', methods=['POST','OPTIONS'])
def createCard():
    if request.method == "OPTIONS":

        return cors_preflight_response()

    else:
        print("1:")
        db = DBConnector(app)
        CONST_TABLENAME = tablenames.CARDS_TABLE
        print("2:")
        input = request.get_json()
        print(request.get_json())

        data = {}
        status_code = statuscodes.STATUS_ERR

        try:
            id = input['id']
            imageKey = input['imageKey']
            imageCategory = input['imageCategory']
            imagePath = input['imagePath']
            imageBackgroundColor = input['imageBackgroundColor']
            recipientName = input['recipientName']
            recipientEmail = input['recipientEmail']
            senderName = input['senderName']
            senderEmail = input['senderEmail']
            sendDate = input['sendDate']
            sendTime = input['sendTime']
            sendTimezone = input['sendTimezone']
            createdDataTime = input['createdDataTime']
            
            query = """INSERT INTO {} 
            (id, imageKey, imageCategory, imagePath, imageBackgroundColor, recipientName, recipientEmail, senderName, 
            senderEmail, sendDate, sendTime, sendTimezone, createdDataTime) 
            VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(CONST_TABLENAME, 
                id, imageKey, imageCategory, imagePath, imageBackgroundColor, recipientName, \
                    recipientEmail, senderName, senderEmail, sendDate, sendTime, sendTimezone, createdDataTime)

            print(query)

            result = db.write(query)

            if len(result) == 0:

                status_code = statuscodes.STATUS_OK 
            
            else: 
                raise ValueError('Unable to create card.')
                
        except Exception as err:
            data = { "Error": str(err) } # something is wrong with the query, either it returns nothing or it returns more than one entry


        response = app.response_class(response=json.dumps(data),
                                    status=status_code,
                                    mimetype='application/json')
        db.__del__()
        return cors_response(response)