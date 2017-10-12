import mysql.connector as mariadb

class MySQLConnection(object):
    def __init__(self, db):
        self.db = mariadb.connect(user='root', password='root', database=db)
        
        # When using SELECT, each row will be returned as a dictionary
        self.cursor = self.db.cursor(dictionary=True) 

    def query_db(self, query, data=None):
        self.cursor.execute(query, data)

        if query[0:6].lower() == 'select':
            return self.cursor.fetchall()
        elif query[0:6].lower() == 'insert':
            self.db.commit()
            return self.cursor.lastrowid
        else:
            self.db.commit()

def MySQLConnector(db):
    return MySQLConnection(db)
