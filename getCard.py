from app import app, request
import json

@app.route('/api/getCard', methods=['GET']) # Flask returns status code 405: The method is not allowed if method is not GET
def getCard():
    cardId = request.args.get('cardId')
    
    data = { 
        "id": cardId,
        "imageKey": "",
        "imageCategory": "",
        "imagePath": "",
        "imageBackgroundColor": "",
        "recipientName": "",
        "recipientEmail": "",
        "senderName": "",
        "senderEmail": "",
        "sendDate": "",
        "sendTime": "",
        "sendTimezone": "" ,
        "createdDataTime": ""
        }

    response = app.response_class(response=json.dumps(data),
                                status=200,
                                mimetype='application/json')
    
    return response