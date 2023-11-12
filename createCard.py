from app import db, app
from flask import request
import json

@app.route('/api/createCard', methods=['POST'])
def createCard():
    CONST_TABLENAME = "Cards"

    id = str(request.args.get('id'))
    imageKey = str(request.args.get('imageKey'))
    imageCategory = str(request.args.get('imageCategory'))
    imagePath = str(request.args.get('imagePath'))
    imageBackgroundColor = str(request.args.get('imageBackgroundColor'))
    recipientName = str(request.args.get('recipientName'))
    recipientEmail = str(request.args.get('recipientEmail'))
    senderName = str(request.args.get('senderName'))
    senderEmail = str(request.args.get('senderEmail'))
    sendDate = str(request.args.get('sendDate'))
    sendTime = str(request.args.get('sendTime'))
    sendTimezone = str(request.args.get('sendTimezone'))
    createdDataTime = str(request.args.get('createdDataTime'))
    
    query = """INSERT INTO {} 
    (id, imageKey, imageCategory, imagePath, imageBackgroundColor, recipientName, recipientEmail, senderName, 
    senderEmail, sendDate, sendTime, sendTimezone, createdDataTime) 
    VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(CONST_TABLENAME, 
        id, imageKey, imageCategory, imagePath, imageBackgroundColor, recipientName, \
            recipientEmail, senderName, senderEmail, sendDate, sendTime, sendTimezone, createdDataTime)

    data = {}
    status_code = 500

    try:
        result = db.write(query)

        if len(result) == 0:

            status_code = 200 
        
        else: 
            raise ValueError('Unable to create card.')
            
    except Exception as err:
        data = { "Error": str(err) } # something is wrong with the query, either it returns nothing or it returns more than one entry


    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    
    return response