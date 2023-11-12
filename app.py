# app.py
from flask import Flask
import mysql.connector

app = Flask(__name__)
app.config.from_pyfile("config.py") # run this before any of the other imports to set up the configuration data

class DBConnector:
    def __init__(self, app):
        self.connection = mysql.connector.connect(
            host=app.config["ENDPOINT"],
            user=app.config["DBUSER"],
            password=app.config["DBPASS"],
            database=app.config["DBNAME"]
        )

    def read(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = self.cursor.fetchall()

        return result

dbConnector = DBConnector(app)


import cardsCatalog

# import createCard

# import getCard

# import getMessages

# import healthcheck

# import signCard

# import testDBconnect

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')