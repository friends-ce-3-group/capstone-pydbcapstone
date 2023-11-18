from endpoint_includes import *
from utils import sendCardImpl

@app.route('/api/createCard', methods=['POST','OPTIONS'])
def createCard():
    if request.method == "OPTIONS":

        return cors_preflight_response()

    else:
        
        db = DBConnector(app)

        CONST_TABLENAME = tablenames.CARDS_TABLE
        
        input = request.get_json()
        
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

            result = db.write(query)

            if len(result) == 0:

                # schedule the card to be sent to the receipient
                data, status_code = sendCardImpl(recipientName, recipientEmail, imagePath, sendDate, sendTime, sendTimezone, app.config)

            else: 
                raise ValueError('Unable to create card.')
                
        except Exception as err:
            data = { "Error": str(err) } # something is wrong with the query


        response = app.response_class(response=json.dumps(data),
                                    status=status_code,
                                    mimetype='application/json')
        
        db.__del__()
        
        return cors_response(response)