from endpoint_includes import *

@app.route('/api/healthcheck', methods=['GET'])
def healthcheck():

    data = {}

    db = DBConnector(app)

    status_code, message = db.healthcheck()

    data["Msg from DB"] = message

    response = app.response_class(response=json.dumps(data),
                                  status=status_code,
                                  mimetype='application/json')
    
    db.__del__()

    return response