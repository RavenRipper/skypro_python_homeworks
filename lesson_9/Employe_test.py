from EmployeeApi import EmployeeApi
from EmployeeSql import EmployeeSQL

api = EmployeeApi("https://x-clients-be.onrender.com")
db = EmployeeSQL("postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")

def test_get_employees():
    
    company_name = "ABN AMRO"
    company_description = "Bank (Netherlands)"
    response = api.create_company(company_name, company_description)
    company_id = response["id"]

    api_employees = api.get_employee(company_id)

    
    db_employees = db.get_employees(company_id)

    
    assert len(api_employees) == len(db_employees), "Employee counts should be equal"

def test_add_employee():
    
    company_name = "ABN AMRO"
    company_description = "Bank (Netherlands)"
    response = api.create_company(company_name, company_description)
    company_id = response["id"]

    
    initial_employees = api.get_employee(company_id)
    initial_count = len(initial_employees)

    
    employee_details = {
        "first_name": "Philipp",
        "last_name": "Kirkorov",
        "middle_name": "Bedrosovich",
        "company_id": company_id,
        "email": "Kirkor666@live.com",
        "phone": "+31612333218"
    }
    new_employee = api.create_employee(**employee_details)
    employee_id = new_employee["id"]

   
    updated_employees = api.get_employee(company_id)
    assert len(updated_employees) == initial_count + 1, "Employee count should have increased by 1"

    
    new_employee_record = next(emp for emp in updated_employees if emp["id"] == employee_id)
    assert all(new_employee_record[key] == value for key, value in employee_details.items()), "Employee details should match"

   
    db.delete(employee_id)

def test_get_single_employee():
    
    company_name = "ABN AMRO"
    company_description = "Bank (Netherlands)"
    response = api.create_company(company_name, company_description)
    company_id = response["id"]

    employee_details = {
        "first_name": "Philipp",
        "last_name": "Kirkorov",
        "middle_name": "Bedrosovich",
        "company_id": company_id,
        "email": "Kirkor666@live.com",
        "phone": "+31612333218"
    }
    db.create(**employee_details)
    employee_id = db.get_max_id()

    
    employee = api.employee_id(employee_id)

    
    assert all(employee[key] == value for key, value in employee_details.items()), "Employee details should match"

    
    db.delete(employee_id)

def test_edit_employee():
    
    company_name = "ABN AMRO"
    company_description = "Bank (Netherlands)"
    response = api.create_company(company_name, company_description)
    company_id = response["id"]

    employee_details = {
        "first_name": "Philipp",
        "last_name": "Kirkorov",
        "middle_name": "Bedrosovich",
        "company_id": company_id,
        "email": "Kirkor666@live.com",
        "phone": "+31612333218"
    }
    db.create(**employee_details)
    employee_id = db.get_max_id()

    
    new_email = "Pugachiha777@live.com"
    updated_employee = api.employee_change(employee_id, new_email=new_email)

    
    assert updated_employee["id"] == employee_id, "Employee ID should match"
    assert updated_employee["email"] == new_email, "Employee email should be updated"

    
    db.delete(employee_id)