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

        cursor.close()

        return result

    def get_table_columns(self,tablename : str) -> list:
        cursor = self.connection.cursor()

        try:
            cursor.execute("SHOW COLUMNS FROM {}".format(tablename))
            columns = cursor.fetchall()
        except:
            columns = []
        
        cursor.close()
        
        return columns


    def __del__(self):
        self.connection.close()

db = DBConnect(app)

#------------------------------------------------

import healthcheck

import cardsCatalog

import getCard

import getMessages



# import createCard





# import signCard

# import testDBconnect

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')