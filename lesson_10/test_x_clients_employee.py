import pytest
from faker import Faker
import allure

from EmployeeApi import EmployeeApi
from EmployeeTable import EmployeeTable
from CompanyTable import CompanyTable


base_url = 'https://x-clients-be.onrender.com'
db_url = 'postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx'

db_emp = EmployeeTable(db_url)
db_com = CompanyTable(db_url)
emp = EmployeeApi(base_url)
fake = Faker("ru_RU")

com_name = f"8_{fake.company()}"
com_desc = fake.catch_phrase()

api_creds_emp = {
    'lastName': fake.last_name(),
    'email': fake.email(),
    'url': fake.url(),
    'phone': fake.random_number(digits=11, fix_len=True),
    'isActive': False
    }


def generate_creds():
    dict_creds_emp = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'middle_name': fake.first_name_male(),
        'is_active': True,
        'phone': fake.random_number(digits=11, fix_len=True),
        'birthdate': fake.date(),
        'url': fake.url()
        }
    return dict_creds_emp


is_active = True

num_emps = 3  # кол-во сотрудников


@allure.epic("hw9")
@allure.feature("сотрудник компании")
class TestEmployee:

    # Создаются одинаковые сотрудники
    @allure.story("получить сотрудника/список сотрудников")
    @allure.title("Получить список сотрудников компании")
    @allure.description("Список сотрудников по id компании")
    @allure.severity("critical")
    def test_get_list_employees(self):
        # создать новую компанию
        db_com.create_company(com_name, com_desc)
        company_id = db_com.get_max_id()

        # проверить что у компании нет сотрудников бд
        list_emp_db = db_emp.get_list_emps_by_id_company(company_id)
        assert len(list_emp_db) == 0

        # создать нескольких сотрудников
        for i in range(num_emps):
            new_creds_emp = generate_creds()
            db_emp.create_employee(company_id, is_active, new_creds_emp)   

        # проверить что создали верное кол-во сотрудников
        with allure.step("Проверить, что созданно заданное кол-во сотрудников"):
            assert len(db_emp.get_list_id_emps_by_id_company(company_id)) == num_emps

        result_api = emp.get_list_employee(params={"company": company_id})
        result_db = db_emp.get_list_emps_by_id_company(company_id)

        with allure.step("Проверить, что длины списков сотрудников одинаковые"):
            assert len(result_api) == len(result_db)

        # сравнить значения ключа id сотрудников,
        # полученных по апи и через запрос к бд
        # считаем, что списки отсортированы по
        # возрастанию по id сотрудника
        with allure.step("Сравнить id сотрудников из БД и через запрос АПИ"):
            for i in range(num_emps):
                assert result_api[i]["id"] == result_db[i]["id"]

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("получить сотрудника/список сотрудников")
    @allure.title("Получить сотрудника компании")
    @allure.description("Создается один сотрудник. Запрос по id сотрудника")
    @allure.severity("critical")
    def test_get_employee_by_id(self):
        # создать новую компанию
        db_com.create_company(com_name, com_desc)
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        new_creds_emp = generate_creds()
        db_emp.create_employee(company_id, is_active, new_creds_emp)

        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        with allure.step("Проверить что создан только 1 сотрудник"):
            assert len(list_id_new_emp) == 1
        id_new_emp = list_id_new_emp[0][0]

        # получить сотрудника по id
        get_new_emp = emp.get_employee_by_id(id_new_emp)

        # проверка значений ключей ответа
        with allure.step("Проверить id сотрудника в БД и в ответе АПИ-метода одинаковые"):
            assert get_new_emp["id"] == id_new_emp

        with allure.step("Проверить firstName сотрудника на соответствие значений полей в БД и через АПИ"):
            assert get_new_emp["firstName"] == list_id_new_emp[0][4]
        with allure.step("Проверить lastName сотрудника на соответствие значений полей в БД и через АПИ"):
            assert get_new_emp["lastName"] == list_id_new_emp[0][5]
        # with allure.step("Проверить email сотрудника {id_new_emp} на соответствие значений полей в БД и через АПИ"):
        #     assert get_new_emp["email"] == list_id_new_emp[0][8]
        # ФР:возвращается null
        # ОР: возвращается значение email
        with allure.step("Проверить isActive сотрудника на соответствие значений полей в БД и через АПИ"):
            assert get_new_emp["isActive"] == list_id_new_emp[0][1]

        with allure.step("Проверить middleName сотрудника на соответствие значений полей в БД и через АПИ"):
            assert get_new_emp["middleName"] == list_id_new_emp[0][6]
        # ФР:ключ avatar_url ОР: ключ url (сваггер)

        with allure.step("Проверить avatar_url сотрудника на соответствие значений полей в БД и через АПИ"):
            assert get_new_emp["avatar_url"] == list_id_new_emp[0][10]
        with allure.step("Проверить phone сотрудника на соответствие значений полей в БД и через АПИ"):    
            assert get_new_emp["phone"] == list_id_new_emp[0][7]

        with allure.step("Проверить birthdate сотрудника {emp_id} на соответствие значений полей в БД и через АПИ"): 
            assert get_new_emp["birthdate"] == list_id_new_emp[0][9].strftime("%Y-%m-%d")

        # проверка что сотрудник есть в списке сотрудников компании
        list_emps = db_emp.get_list_emps_by_id_company(company_id)
        emp_list_id = list_emps[-1][0]
        with allure.step("Проверить сотрудник с id есть в списке сотрудников компании"):
            assert emp_list_id == get_new_emp["id"]

        # удаление сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative.получить сотрудника/список сотрудников")
    @allure.title("Получить сотрудника компании без id")
    @allure.description("Создается один сотрудник. Отправляется АПИ запрос без id")
    @allure.severity("Minor")
    def test_get_employee_by_id_without_id(self):
        # создать новую компанию
        db_com.create_company(com_name, com_desc)
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        new_creds_emp = generate_creds()
        db_emp.create_employee(
            company_id, is_active, new_creds_emp)

        # получить сотрудника по id
        get_new_emp = emp.get_employee_by_id_without_id()
        with allure.step("Проверить статус-код ответа"):
            assert get_new_emp["statusCode"] == 500
        with allure.step("Проверить текст статус-кода ответа"):
            assert get_new_emp["message"] == 'Internal server error'
        # необходимо прописать более информационный статус код и сообщение.
        # возможно 400 - плохой запрос

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("создание сотрудника/сотрудников")
    @allure.title("Создать нового сотрудника компании")
    @allure.description("Создается один сотрудник. Запрос по id сотрудника")
    @allure.severity("blocker")
    def test_create_employee(self):
        # создать новую компанию
        db_com.create_company(com_name, com_desc)
        company_id = db_com.get_max_id()

        # проверить, что у созданной компании нет работников
        emp_list_f = db_emp.get_list_emps_by_id_company(company_id)
        len_before = len(emp_list_f)

        with allure.step("Проверить, что у новой компании нет сотрудников"):
            assert len_before == 0

        # создать нового работника
        new_creds_emp = generate_creds()
        db_emp.create_employee(company_id, is_active, new_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        # проверка, что создан 1 работник
        emp_list = db_emp.get_list_emps_by_id_company(company_id)
        len_after = len(emp_list)

        with allure.step("Проверить, что создан сотрудник"):
            assert len_after - len_before == 1

        # проверка созданного работника
        result_api = emp.get_employee_by_id(id_new_emp)

        # проверка заполненных
        with allure.step("Проверить id сотрудника на соответствие значений полей в БД и через АПИ"):
            assert result_api["id"] == id_new_emp
        with allure.step("Проверить firstName сотрудника на соответствие значений полей в БД и через АПИ"):    
            assert result_api["firstName"] == new_creds_emp["first_name"]
        with allure.step("Проверить lastName сотрудника на соответствие значений полей в БД и через АПИ"):
            assert result_api["lastName"] == new_creds_emp["last_name"]
        with allure.step("Проверить isActive сотрудника на соответствие значений полей в БД и через АПИ"):
            assert result_api["isActive"] is True

        # - не сохраняется значение
        # with allure.step("Проверить email сотрудника на соответствие значений полей в БД и через АПИ"):
        #     assert result_api["email"] == new_creds_emp["email"]
        with allure.step("Проверить middleName сотрудника на соответствие значений полей в БД и через АПИ"):
            assert result_api["middleName"] == new_creds_emp["middle_name"]
        with allure.step("Проверить avatar_url сотрудника на соответствие значений полей в БД и через АПИ"):
            assert result_api["avatar_url"] == new_creds_emp["url"]
        with allure.step("Проверить phone сотрудника на соответствие значений полей в БД и через АПИ"):
            assert result_api["phone"] == str(new_creds_emp["phone"])
        with allure.step("Проверить birthdate сотрудника на соответствие значений полей в БД и через АПИ"):
            assert result_api["birthdate"] == new_creds_emp["birthdate"]

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative.создание сотрудника/сотрудников")
    @allure.title("Создать нового сотрудника компании без токена авторизации")
    @allure.description("")
    @allure.severity("Major")
    def test_create_employee_without_auth_token(self):
        # создать новую компанию
        db_com.create_company(com_name, com_desc)
        company_id = db_com.get_max_id()

        # проверить что у созданной компании нет сотрудника
        emp_list_f = db_emp.get_list_emps_by_id_company(company_id)
        len_before = len(emp_list_f)
        with allure.step("Проверить, что у новой компании нет сотрудников"):
            assert len(emp_list_f) == 0

        # создать нового сотрудника
        new_creds_emp = generate_creds()
        new_emp = emp.create_employee_without_auth_token(
            company_id, new_creds_emp)
        with allure.step("Проверить статус-код ответа"):
            assert new_emp["statusCode"] == 401
        with allure.step("Проверить текст статус-кода ответа"):  
            assert new_emp["message"] == 'Unauthorized'

        # проверка, что не создан сотрудник
        emp_list_a = db_emp.get_list_emps_by_id_company(company_id)
        len_after = len(emp_list_a)
        with allure.step("Проверить, что новый сотрудник не создан"):
            assert len_after - len_before == 0

        # удаление компании
        db_com.delete_company(company_id)

    @allure.story("negative.создание сотрудника/сотрудников")
    @allure.title("Создать нового сотрудника компании без тела запроса")
    @allure.description("")
    @allure.severity("Major")
    def test_create_employee_without_body(self):
        # создать новую компанию
        db_com.create_company(com_name, com_desc)
        company_id = db_com.get_max_id()

        # проверка что у созданной компании нет сотрудников
        emp_list_f = db_emp.get_list_emps_by_id_company(company_id)
        with allure.step("Проверить, что у новой компании нет сотрудников"):
            assert len(emp_list_f) == 0

        # создать нового сотрудника
        new_emp = emp.create_employee_without_body()
        with allure.step("Проверить статус-код ответа"):
            assert new_emp["statusCode"] == 500
        with allure.step("Проверить текст статус-кода ответа"):
            assert new_emp["message"] == 'Internal server error'
        # необходимо прописать более информационный статус код и сообщение.
        # возможно 400 - плохой запрос

        # удаление компании
        db_com.delete_company(company_id)

    # есть вопросы
    @allure.story("редактировать сотрудника/сотрудников")
    @allure.title("Изменить сотрудника компании")
    @allure.description("")
    @allure.severity("blocker")
    def test_patch_employee(self):
        # создать новую компанию
        db_com.create_company(com_name, com_desc)
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        new_creds_emp = generate_creds()
        db_emp.create_employee(company_id, is_active, new_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        new_creds_emp = generate_creds()
        db_emp.patch_employee(id_new_emp, is_active, new_creds_emp)
        result_db = db_emp.get_emp_by_id(id_new_emp)

        # проверить ключи ответа - ФР: нет ключей прописанных в свагере
        # ОР: все ключи есть в json
        result_api = emp.get_employee_by_id(id_new_emp)
        
        with allure.step("Проверить id сотрудника на соответствие значений полей в БД и через АПИ"):
            assert result_db[0][0] == result_api.get("id")

        with allure.step("Проверить lastName сотрудника на соответствие значений полей в БД и через АПИ"):
            assert result_db[0][5] == result_api.get('lastName')
        # ФР: ключ-значение не возвращается
        # ОР: ключ - значение (новое)
        with allure.step("Проверить isActive сотрудника на соответствие значений полей в БД и через АПИ"):
            assert result_db[0][1] == result_api.get('isActive')
        with allure.step("Проверить email сотрудника на соответствие значений полей в БД и через АПИ"):
            assert result_db[0][8] == result_api.get('email')
        # with allure.step("Проверить phone сотрудника на соответствие значений полей в БД и через АПИ"):
        # assert result_db[0][7] == result_api.get('phone')
        # ФР: ключ-значение не возвращается
        # ОР: ключ - значение (новое)
        with allure.step("Проверить avatar_url сотрудника на соответствие значений полей в БД и через АПИ"):
            assert result_db[0][10] == result_api.get('avatar_url')

        # with allure.step("Проверить firstName сотрудника на соответствие значений полей в БД и через АПИ"):
        # assert result_db[0][4] == result_api['firstName']
        # ФР: ключ-значение не возвращается
        # ОР: ключ - значение
        with allure.step("Проверить middleName сотрудника на соответствие значений полей в БД и через АПИ"):
            assert result_db[0][6] == result_api.get('middleName')
        with allure.step("Проверить companyId сотрудника на соответствие значений полей в БД и через АПИ"):
            assert result_db[0][11] == result_api.get('companyId')
        with allure.step("Проверить birthdate сотрудника на соответствие значений полей в БД и через АПИ"):
            assert result_db[0][9].strftime("%Y-%m-%d") == result_api.get('birthdate')
        
        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative.редактировать сотрудника/сотрудников")
    @allure.title("Изменить сотрудника компании без токена авторизации")
    @allure.description("")
    @allure.severity("Major")
    def test_patch_employee_without_auth_token(self):
        # создать новую компанию
        db_com.create_company(com_name, com_desc)
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        new_creds_emp = generate_creds()
        db_emp.create_employee(company_id, is_active, new_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        result = emp.change_info_employee_without_auth_token(
            id_new_emp, api_creds_emp)
        
        with allure.step("Проверить статус-код ответа"):
            assert result["statusCode"] == 401
        with allure.step("Проверить текст статус-кода ответа"):
            assert result["message"] == 'Unauthorized'

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @allure.story("negative.редактировать сотрудника/сотрудников")
    @allure.title("Изменить сотрудника компании без id сотрудника")
    @allure.description("")
    @allure.severity("Major")
    def test_patch_employee_without_id(self):
        # создать новую компанию
        db_com.create_company(com_name, com_desc)
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        new_creds_emp = generate_creds()
        db_emp.create_employee(company_id, is_active, new_creds_emp)

        result = emp.change_info_employee_without_id(api_creds_emp)

        with allure.step("Проверить статус-код ответа"):
            assert result["statusCode"] == 404
        with allure.step("Проверить текст статус-кода ответа"):
            assert result["error"] == 'Not Found'

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @pytest.mark.xfail(reason="без тела запроса возвращается информация по пользователю")
    @allure.story("negative.редактировать сотрудника/сотрудников")
    @allure.title("Изменить сотрудника компании без тела запроса")
    @allure.description("")
    @allure.severity("Major")
    def test_patch_employee_without_body(self):
        # создать новую компанию
        db_com.create_company(com_name, com_desc)
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        new_creds_emp = generate_creds()
        db_emp.create_employee(company_id, is_active, new_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        result = emp.change_info_employee_without_body(
            id_new_emp)

        with allure.step("Проверить статус-код ответа"):
            assert result["statusCode"] == 404
        with allure.step("Проверить текст статус-кода ответа"): 
            assert result["error"] == 'Not Found'

        # удалить сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_company(company_id)

    @pytest.mark.xfail(reason="ФР: 500, ОР: 404")
    @allure.story("negative.редактировать сотрудника/сотрудников")
    @allure.story("negative.редактировать сотрудника/сотрудников")
    @allure.title("Изменить сотрудника компании с некорректным id")
    @allure.description("")
    @allure.severity("Major")
    def test_patch_employee_wrong_id(self):
        # создать новую компанию
        db_com.create_company(com_name, com_desc)
        company_id = db_com.get_max_id()

        # создать нового сотрудника
        new_creds_emp = generate_creds()
        db_emp.create_employee(company_id, is_active, new_creds_emp)
        list_id_new_emp = db_emp.get_list_emps_by_id_company(company_id)
        id_new_emp = list_id_new_emp[0][0]

        wrong_emp_id = id_new_emp + 1000

        result = emp.change_info_employee_wrong_id(wrong_emp_id)

        with allure.step("Проверить статус-код ответа"):
            assert result["statusCode"] == 404
        with allure.step("Проверить текст статус-кода ответа"): 
            assert result["message"] == 'Not Found'

        # удаление сотрудников и компании
        db_emp.delete_list_emps_by_company_id(company_id)
        db_com.delete_soft(company_id)
