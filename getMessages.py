from app import app, request
import json

@app.route('/api/getMessages', methods=['GET'])
def getMessages():
    data = {
        "message":"nothing to see here. Add something at the end."
    }
    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    
    return response