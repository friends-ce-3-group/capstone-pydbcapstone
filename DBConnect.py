from app import app as flaskapp
import mysql.connector

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



dbConnector = DBConnector(flaskapp)