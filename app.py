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

    def write(self, query : str) -> list:
        cursor = self.connection.cursor()
        
        cursor.execute(query)
        
        self.connection.commit()
        
        result = cursor.fetchall()
        
        cursor.close()

        return result

    def get_table_columns(self, tablename : str) -> list:
        cursor = self.connection.cursor()

        try:
            cursor.execute("SHOW COLUMNS FROM {}".format(tablename))
            columns = cursor.fetchall()
        except:
            columns = []
        
        cursor.close()
        
        return columns

    def processed_read_data(self, tablename : str, query : str) -> dict:
        data = {}
        status_code = 500

        result = db.read(query)

        if result:
            if len(result) == 1: 

                columns = db.get_table_columns(tablename)
    
                for col, entry in zip(columns, result[0]):
                    key_name = col[0]
                    data[key_name] = entry

            else:
                columns = db.get_table_columns(tablename)

                for idx, found in enumerate(result):
                    entry_data = {}
                    for col, entry in zip(columns, found):
                        key_name = col[0]
                        entry_data[key_name] = entry

                    data[idx] = entry_data

            status_code = 200


        return data, status_code

    def __del__(self):
        self.connection.close()

db = DBConnect(app)

#------------------------------------------------

import healthcheck

import cardsCatalog

import getCard

import getMessages

import createCard

import signCard



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')