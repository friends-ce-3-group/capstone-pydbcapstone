from endpoint_includes import *

@app.route('/api/healthcheck', methods=['GET'])
def healthcheck():

    data = {"Performing healthcheck" : "/api/healthcheck"}
    status_code = statuscodes.STATUS_OK

    response = app.response_class(response=json.dumps(data),
                                  status=status_code,
                                  mimetype='application/json')
    
    return response