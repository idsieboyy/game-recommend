from configparser import ConfigParser
import psycopg2


def load_config(filename='db.ini', section='postgresql'):
    """Reads the config file with the database login information"""
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db


class DatabaseManager:
    conn = None

    def connect(self):
        """Connect to the database specified in db.ini"""
        try:
            params = load_config()
            self.conn = psycopg2.connect(**params)
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def close(self):
        """Close the connection to the database, this must be called before the program exits"""
        if self.conn is not None:
            self.conn.close()

    def get_genres(self):
        result = None
        try:
            cursor = self.conn.cursor()
            cursor.execute('')  # TODO Add the right statement
            result = cursor.fetchall()
            cursor.close()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        return result

    def get_tags(self):
        result = None
        try:
            cursor = self.conn.cursor()
            cursor.execute('')  # TODO Add the right statement
            result = cursor.fetchall()
            cursor.close()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        return result

    def get_games_with_genre(self, genre):
        result = None
        try:
            cursor = self.conn.cursor()
            cursor.execute('', genre)  # TODO Add the right statement
            result = cursor.fetchall()
            cursor.close()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        return result
