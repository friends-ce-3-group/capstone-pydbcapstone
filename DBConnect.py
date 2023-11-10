from app import app
import mysql.connector

class DBConnector:
    def __init__(self, app):
        self.connection = mysql.connector.connect(
            host=app.config["ENDPOINT"],
            user=app.config["DBUSER"],
            password=app.config["DBPASS"],
            database=app.config["DBNAME"]
        )

        self.cursor = self.connection.cursor()


    def execute(self, query):
        self.cursor.execute(query)

        result = self.cursor.fetchall()

        return result
    
    
dbConnector = DBConnector(app)