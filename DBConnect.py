from app import app
import mysql.connector


def db_read(query):
    
    connection = mysql.connector.connect(
        host=app.config["ENDPOINT"],
        user=app.config["DBUSER"],
        password=app.config["DBPASS"],
        database=app.config["DBNAME"]
    )
    cursor = connection.cursor()
    
    cursor.execute(query)

    result = cursor.fetchall()

    connection.close()

    return result
