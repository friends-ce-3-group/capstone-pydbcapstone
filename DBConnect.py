# from app import app
# from mysql import connector

# def get_cursor() -> connector.MySQLCursor:

#     connection = connector.connect(
#         host=app.config["ENDPOINT"],
#         user=app.config["DBUSER"],
#         password=app.config["DBPASS"],
#         database=app.config["DBNAME"]
#     )
#     cursor = connection.cursor()

#     return cursor

# def db_read(query: str) -> list:

#     cursor = get_cursor()

#     cursor.execute(query)

#     result = cursor.fetchall()

#     return result

# def get_table_columns(tablename : str) -> list:
#     cursor = get_cursor()

#     try:
#         cursor.execute("SHOW COLUMNS FROM {}".format(tablename))
#         columns = cursor.fetchall()
#     except:
#         columns = []
    
#     cursor.close()

#     return columns