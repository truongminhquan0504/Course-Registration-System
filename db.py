import pyodbc

def get_db_connection():
    
    server = 'localhost\\SQLEXPRESS' 
    database = 'CourseRegistrationDB'
    
    connection_string = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
    )
    
    
    conn = pyodbc.connect(connection_string)
    return conn