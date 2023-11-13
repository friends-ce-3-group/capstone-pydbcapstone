from mysql import connector
import statuscodes

class DBConnector:
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

        # helper function
        #---------------------------------------------------------
        def populate(columns, found):
            entry_data = {}
            for col, entry in zip(columns, found):
                key_name = col[0]
                entry_data[key_name] = entry
            return entry_data
        #---------------------------------------------------------

        data = {}
        status_code = statuscodes.STATUS_ERR

        result = self.read(query)

        if result:
            columns = self.get_table_columns(tablename)

            if len(result) == 1: 
                data = populate(columns, result[0])
            else:
                for idx, found in enumerate(result):
                    data[idx] = populate(columns, found)

            status_code = statuscodes.STATUS_OK


        return data, status_code

    def __del__(self):
        self.connection.close()