from sqlalchemy import create_engine, text

class EmployeeSQL:
    
    __scripts = {
        "select_by_id_company": text("SELECT * FROM employee WHERE company_id = :company_id"),
        "delete_by_id": text("DELETE FROM employee WHERE id = :id_to_delete"),
        "insert_new": text("""
            INSERT INTO employee (first_name, last_name, middle_name, company_id, email, phone)
            VALUES (:first_name, :last_name, :middle_name, :company_id, :email, :phone)
        """),
        "get_max_id": text("SELECT MAX(id) FROM employee")
    }

    def __init__(self, connection_string):
        self.__engine = create_engine(connection_string)
    
    def get_employees(self, company_id):
        with self.__engine.connect() as connection:
            result = connection.execute(self.__scripts["select_by_id_company"], {"company_id": company_id})
            return result.fetchall()

    def delete(self, employee_id):
        with self.__engine.connect() as connection:
            connection.execute(self.__scripts["delete_by_id"], {"id_to_delete": employee_id})
            connection.commit()

    def create(self, first_name, last_name, middle_name, company_id, email, phone):
        with self.__engine.connect() as connection:
            connection.execute(self.__scripts["insert_new"], {
                "first_name": first_name,
                "last_name": last_name,
                "middle_name": middle_name,
                "company_id": company_id,
                "email": email,
                "phone": phone
            })
            connection.commit()

    def get_max_id(self):
        with self.__engine.connect() as connection:
            result = connection.execute(self.__scripts["get_max_id"])
            return result.scalar()  
