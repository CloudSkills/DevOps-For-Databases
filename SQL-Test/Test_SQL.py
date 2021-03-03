import mysql.connector
from mysql.connector import errorcode
import sys


def testdb():
    try:
        connect = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database
        )

        cursor = connect.cursor()

        cursor.execute("SELECT FirstName FROM users")
        result = cursor.fetchall()

        for query in result:
            print(query)

        connect.close()

    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access Denied for this user")



user = sys.argv[1]
password = sys.argv[2]
host = sys.argv[3]
database = sys.argv[4]


if __name__ == '__main__':
    testdb()
