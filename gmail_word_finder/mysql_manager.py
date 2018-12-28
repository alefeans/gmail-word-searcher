import sys
import mysql.connector
from mysql.connector import errorcode


class MySQLConnector:

    def __init__(self, user, password, address):
        self.user = user
        self.password = password
        self.address = address
        self.connection = self._get_connection()
        self.cursor = self.connection.cursor()
        self._db_email()

    def _get_connection(self):
        """
        Returns the connection with MySQL using
        the user parameters.
        """
        try:
            connection = mysql.connector.connect(user=self.user,
                                                 password=self.password,
                                                 host=self.address)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("ERROR - Wrong username or password")
                sys.exit()
            else:
                print("ERROR - {}".format(err))
                sys.exit()
        else:
            return connection

    def _create_database(self):
        try:
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS emails")
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print("ERROR - Failed creating database: {}".format(err))
            self._close_resources(self.connection, self.cursor)
            sys.exit()

    def _create_table(self):
        try:
            self.cursor.execute("USE emails")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS mail_list(
                      id_email INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
                      date CHAR(45) NOT NULL,
                      origin CHAR(90) NOT NULL,
                      subject CHAR(255) NOT NULL)""")
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print("ERROR - Failed creating table: {}".format(err))
            self._close_resources(self.connection, self.cursor)
            sys.exit()

    def _close_resources(self, connection, cursor):
        cursor.close()
        connection.close()
        return

    def _db_email(self):
        """
        Checks if both database and tables were
        created successfully and close the
        'connection' and 'cursor'.
        """
        if self._create_database() and self._create_table():
            print("INFO - Database 'emails' and table 'mail_list' OK")
        self._close_resources(self.connection, self.cursor)

    def insert_items(self, content):
        """
        Receives the 'content' object and makes the
        insertion in the database. All the inserted
        items are printed.
        """
        query = "INSERT INTO mail_list(date, origin, subject)" \
                "VALUES (%s, %s, %s)"
        args = (content['Date'], content['From'], content['Subject'])
        try:
            connection = self._get_connection()
            cursor = connection.cursor()
            cursor.execute("USE emails")
            cursor.execute(query, args)
            connection.commit()
            print("INFO - Inserting {} on table 'mail_list'".format(args))
        except mysql.connector.Error as err:
            print(err)
        finally:
            self._close_resources(connection, cursor)


if __name__ == '__main__':
    pass
