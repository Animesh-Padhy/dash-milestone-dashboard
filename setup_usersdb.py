import sqlite3


def setup_database():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    command = """CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT)"""
    cursor.execute(command)
    cursor.execute("INSERT INTO users VALUES ('admin1','test1234')")
    connection.commit()
    connection.close()


if __name__ == "__main__":
    setup_database()
