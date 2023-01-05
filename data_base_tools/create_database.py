import sqlite3


def connect_database(db_path: str = r"E:\PYTHON PROGRAMMS\DjangoProject_For_View_Files\db.sqlite3") -> tuple:
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    return connection, cursor


class InitDataBase:
    def __init__(self):
        self.connection, self.cursor = connect_database()

    def create_file_names(self):
        self.cursor.execute("""CREATE TABLE new_from_db_files 
        (id integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
        company_name varchar(40) NOT NULL, 
        qty varchar(40) NOT NULL, 
        file_name varchar(65) NULL, 
        plate_size varchar(40) NOT NULL, 
        equipment varchar(40) NOT NULL, 
        add_date_time datetime NOT NULL, 
        punch varchar(255) NOT NULL, 
        stage varchar(255) NOT NULL, 
        operator varchar(255) NOT NULL, 
        ready_datetime datetime NULL)
        """)

    def init(self):
        self.create_file_names()
        self.connection.commit()
        self.connection.close()


if __name__ == "__main__":
    InitDataBase().init()
