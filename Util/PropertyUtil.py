class PropertyUtil:

    @staticmethod
    def getPropertyString():
        host = "LAPTOP-9SK29CK2\SQLEXPRESS"
        dbname = "Project_Management_System"
        
        # return f'DRIVER={{SQL Server}};SERVER={host};DATABASE={dbname};UID={username};PWD={password};PORT={port}'
        return f'DRIVER={{SQL Server}};SERVER={host};DATABASE={dbname};Trusted_Connection=yes;'


# 'Driver={SQL Server};'
#                     'Server=LAPTOP-9SK29CK2\SQLEXPRESS;'
#                     'Database=Order_Management_System;'
#                     'Trusted_Connection=yes;'