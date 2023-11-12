# app.py
from flask import Flask
from mysql import connector
import json

app = Flask(__name__)
app.config.from_pyfile("config.py") # run this before any of the other imports to set up the configuration data

class DBConnect:
    def __init__(self, app):
        self.connection = connector.connect(
            host=app.config["ENDPOINT"],
            user=app.config["DBUSER"],
            password=app.config["DBPASS"],
            database=app.config["DBNAME"]
        )

    def read(self, query : str) -> list:
        cursor = self.connection.cursor()

        cursor.execute(query)

        result = cursor.fetchall()

        return result

db = DBConnect(app)


@app.route('/api/cardsCatalog', methods=['GET'])
def cardsCatalog():

    query = """SELECT * FROM cardsCatalog"""

    result = db.read(query)

    response = app.response_class(response=json.dumps(result),
                                status=200,
                                mimetype='application/json')

    return response




# import cardsCatalog

# import createCard

# import getCard

# import getMessages

# import healthcheck

# import signCard

# import testDBconnect

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')