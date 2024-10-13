import pyodbc

class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        try:
            if DBConnection.connection is None:
                from Util.PropertyUtil import PropertyUtil
                connection_string = PropertyUtil.getPropertyString()
                DBConnection.connection = pyodbc.connect(connection_string)
                print("DB Connected")
                print(DBConnection.connection)
                return DBConnection.connection
            
        
        except Exception as error:
            print("ERROR:  {}".format(error))

# o= DBConnection()
# o.getConnection()
