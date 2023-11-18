from endpoint_includes import *

@app.route('/api/getMessages', methods=['GET','OPTIONS'])
def getMessages():
    if request.method == "OPTIONS":

        return cors_preflight_response()

    else:
        db = DBConnector(app)
        
        CONST_TABLENAME = tablenames.MESSAGES_TABLE

        cardId = str(request.args.get('cardId'))

        query = "SELECT * FROM {0} WHERE cardId = '{1}'".format(CONST_TABLENAME, cardId)

        data = {}
        status_code = statuscodes.STATUS_ERR

        try:
            data, status_code = db.processed_read_data(CONST_TABLENAME, query)

            if status_code == statuscodes.STATUS_ERR:
                raise ValueError('No entry found for cardId {}.'.format(cardId))
            
        except Exception as err:
            data = { "Error": str(err) } # something went wrong with the query



        response = app.response_class(response=json.dumps(data),
                                    status=status_code,
                                    mimetype='application/json')
        
        db.__del__()

        return cors_response(response)