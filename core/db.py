import sqlite3
import config

class DB:
    def __init__(self):
        self.conn = sqlite3.connect(config.db_name)
        self.c = self.conn.cursor()

        if self.conn is not None:
            self.c.execute(config.CREATE_TABLES)
        else:
            print("Cannot create database connection!")

    def find(self, id):
        if self.c.execute(config.FIND_RECORD, (id,)).fetchone()[0] == 0:
            return False
        
        return True

    def add(self, values):
        print(f'Inserted {values} into the DB')
        self.c.execute(config.INSERT_RECORD, values)

    def remove(self, id):
        self.c.execute(config.DELETE_RECORD, (id,))