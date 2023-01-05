from .create_database import connect_database


class BaseTools:
    def __init__(self):
        self.connection, self.cursor = connect_database(r"E:\PYTHON PROGRAMMS\DjangoProject_For_View_Files\db.sqlite3")


class DataBaseTools(BaseTools):
    def insert_plate_info_in_table(self, company_name, qty, file_name, plate_size, equipment, add_date_time, punch,
                                   stage, operator, ready_datetime):
        try:
            self.cursor.execute("""INSERT INTO new_from_db_files(
            company_name, 
            qty, 
            file_name, 
            plate_size, 
            equipment, 
            add_date_time, 
            punch, 
            stage, 
            operator, 
            ready_datetime)
            VALUES (?,?,?,?,?,?,?,?,?,?) 
            """, (
                company_name,
                qty,
                file_name,
                plate_size,
                equipment,
                add_date_time,
                punch,
                stage,
                operator,
                ready_datetime))
        except:
            pass
        else:
            self.connection.commit()
        finally:
            self.connection.close()
