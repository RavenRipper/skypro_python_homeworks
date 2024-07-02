import requests
import allure


class EmployeeApi:

    user = 'bloom'
    password = 'fire-fairy'

    def __init__(self, url):
        self.url = url

    @allure.step("api.получить токен авторизации")
    def get_token(self, user=user, password=password) -> str:
        """
        Метод получает токен для авторизации.
        """
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]

    @allure.step("api.создать нового сотрудника компании")
    def create_employee(
            self, company_id: int, first_name: str, last_name: str,
            email: str, isActive: bool, id=1,
            middle_name='', url='', phone='',
            birthdate='2005-05-03') -> dict:
        """
        Метод создает нового сотрудника компании.
        """
        creds = {
            'id': id,
            'firstName': first_name,
            'lastName':  last_name,
            'middleName': middle_name,
            'companyId': company_id,
            'email': email,
            'url': url,
            'phone': phone,
            'birthdate': birthdate,
            'isActive': isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(
            self.url + '/employee', headers=my_headers, json=creds)
        return resp.json()

    @allure.step("api.создать несколько - {num_emp} новых сотрудников компании")
    def create_list_employee_get_list_id(
            self, num_emp, company_id, first_name, last_name,
            email, isActive, id=1,
            middle_name='', url='', phone='',
            birthdate='2005-05-03T11:19:37.153Z') -> list:
        list_new_emp = []
        list_new_emp_id = []
        creds = {
            'id': id,
            'firstName': first_name,
            'lastName':  last_name,
            'middleName': middle_name,
            'companyId': company_id,
            'email': email,
            'url': url,
            'phone': phone,
            'birthdate': birthdate,
            'isActive': isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        for i in range(num_emp):
            resp = requests.post(
                self.url + '/employee', headers=my_headers, json=creds)
            resp_json = resp.json()
            list_new_emp.append(resp_json)

        for i in range(len(list_new_emp)):
            emp_full = list_new_emp[i]["id"]
            list_new_emp_id.append(emp_full)

        return list_new_emp_id

    @allure.step("api.создать сотрудника без токена авторизации")
    def create_employee_without_auth_token(
            self, company_id: int, dict_creds_emp: dict) -> dict:
        """
        Метод для проверки возможности создания сотрудника компании
        без токена авторизации.
        """
        resp = requests.post(
            self.url + '/employee', json=dict_creds_emp)
        return resp.json()

    @allure.step("api.создать сотрудника без тела запроса")
    def create_employee_without_body(self) -> dict:
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(
            self.url + '/employee', headers=my_headers)
        return resp.json()

    @allure.step("api.получить список сотрудников по параметру - {params}")
    def get_list_employee(self, params: dict) -> list:
        """
        Метод возвращает список словарей с данными сотрудников,
        соответствующих определенному параметру.
        """
        resp = requests.get(self.url + '/employee', params)
        return resp.json()

    @allure.step("api.получить сотрудника по id {emp_id}")
    def get_employee_by_id(self, emp_id: int) -> dict:
        """
        Метод получает словарь с информацией о сотруднике по id.
        """
        resp = requests.get(self.url + '/employee/' + str(emp_id))
        return resp.json()

    @allure.step("api.получить сотрудника по id без id")
    def get_employee_by_id_without_id(self) -> dict:
        resp = requests.get(self.url + '/employee/')
        return resp.json()

    @allure.step("api.изменить информацию о сотруднике - {cred}")
    def change_info_employee(
            self, emp_id: int, api_creds_emp: dict) -> dict:
        """
        Метод находит сотрудника по id и изменяет значение полей.
        """
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.patch(
            self.url + '/employee/' + str(emp_id), headers=my_headers,
            json=api_creds_emp)
        return resp.json()

    @allure.step("api.изменить информацию о сотруднике без токена авторизации")
    def change_info_employee_without_auth_token(
            self, emp_id: int, api_creds_emp: dict) -> dict:

        resp = requests.patch(
            self.url + '/employee/' + str(emp_id),
            json=api_creds_emp)
        return resp.json()

    @allure.step("api.изменить информацию о сотруднике без id")
    def change_info_employee_without_id(
            self, api_creds_emp: dict) -> dict:
  
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.patch(
            self.url + '/employee/', headers=my_headers,
            json=api_creds_emp)
        return resp.json()

    @allure.step("api.изменить информацию о сотруднике без тела запроса")
    def change_info_employee_without_body(
            self, emp_id: int) -> dict:

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.patch(
            self.url + '/employee/' + str(emp_id), headers=my_headers)
        return resp.json()

    @allure.step("api.изменить информацию о сотруднике с несущест. id")
    def change_info_employee_wrong_id(
            self, emp_id: int) -> dict:

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.patch(
            self.url + '/employee/' + str(emp_id), headers=my_headers)
        return resp.json()
    
