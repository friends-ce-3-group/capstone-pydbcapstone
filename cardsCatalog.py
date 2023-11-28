from endpoint_includes import *

@app.route('/api/cardsCatalog', methods=['GET','OPTIONS'])
def cardsCatalog():
    if request.method == "OPTIONS":

        return cors_preflight_response()

    else:
        db = DBConnector(app)

        print("PROXYENDPOINT: ", app.config["PROXYENDPOINT"])

        CONST_TABLENAME = tablenames.CARDS_CATALOG_TABLE

        query = "SELECT * FROM {}".format(CONST_TABLENAME)

        data = {}
        status_code = statuscodes.STATUS_ERR
        
        try:
            data, status_code = db.processed_read_data(CONST_TABLENAME, query)

            status_code = statuscodes.STATUS_OK

        except Exception as err:
            data = { "Error": str(err) }


        response = app.response_class(response=json.dumps(data),
                                    status=status_code,
                                    mimetype='application/json')
        
        db.__del__()

        return cors_response(response)