import requests

class EmployeeApi:
    def __init__(self, url):
        self.url = url
        self.user_token = None

    def authenticate(self, user='flora', password='nature-fairy'):
        if not self.user_token:
            creds = {"username": user, "password": password}
            response = requests.post(f"{self.url}/auth/login", json=creds)
            self.user_token = response.json()["userToken"]
        return self.user_token

    def create_company(self, name, description=""):
        company_data = {"name": name, "description": description}
        headers = {"x-client-token": self.authenticate()}
        response = requests.post(f"{self.url}/company", json=company_data, headers=headers)
        return response.json()

    def get_employees(self, company_id):
        response = requests.get(f"{self.url}/employee?company={company_id}")
        return response.json()

    def create_employee(self, first_name, last_name, middle_name, company_id, email, url, phone):
        employee_data = {
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "companyId": company_id,
            "email": email,
            "url": url,
            "phone": phone
        }
        headers = {"x-client-token": self.authenticate()}
        response = requests.post(f"{self.url}/employee", json=employee_data, headers=headers)
        return response.json()

    def get_employee_by_id(self, employee_id):
        response = requests.get(f"{self.url}/employee/{employee_id}")
        return response.json()

    def update_employee(self, employee_id, last_name=None, email=None, url=None, phone=None):
        updates = {
            "lastName": last_name,
            "email": email,
            "url": url,
            "phone": phone
        }
        updates = {k: v for k, v in updates.items() if v is not None}
        headers = {"x-client-token": self.authenticate()}
        response = requests.patch(f"{self.url}/employee/{employee_id}", json=updates, headers=headers)
        return response.json()