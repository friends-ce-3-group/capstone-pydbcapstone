from app import app
import json

@app.route('/api/createCard', methods=['POST'])
def createCard():
    data = {}
    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    
    return response