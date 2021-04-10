#!/usr/bin/python

import sqlite3

def exec_db(sql_statement):

        result = []

        conn = sqlite3.connect('pwmdb.db')
        cur = conn.cursor()
        cur.execute(sql_statement)

        if sql_statement[0] == 'i' or sql_statement[0] == 'd' or sql_statement[0] == 'u' or sql_statement[0] == 'c':
            conn.commit()
            
        elif sql_statement[0] == 's':
            
            for item in cur:
                result.append(item)

        conn.close()

        return result