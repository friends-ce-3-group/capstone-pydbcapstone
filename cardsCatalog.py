from app import db, app
import cors
import json

@app.route('/api/cardsCatalog', methods=['OPTIONS','GET'])
def cardsCatalog():
    if request.method == "OPTIONS":
        return cors_preflight_response()
    else:            
        query = """SELECT * FROM cardsCatalog"""

        data = {}
        status_code = 500

        try:
            data = db.read(query)

            status_code = 200

        except Exception as err:
            data = { "Error": str(err) }


        response = app.response_class(response=json.dumps(data),
                                    status=status_code,
                                    mimetype='application/json')

        return response