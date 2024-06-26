import pytest
import requests
import json
from lesson_8.Pages.Employee import Employer, Company
from lesson_8.constants import x_client_URL

employer = Employer()
company = Company()

def test_auth(get_token): 
    token = get_token
    assert token is not None #Проверяю, что токен не пустой
    assert isinstance(token, str) #Проверяю, что токен имеет строковый формат

def test_getcompany_id():
    company_id = company.last_active_company_id()
    assert company_id is not None #Проверяю, что id компании не пустое
    assert str(company_id).isdigit() #Проверяю, что id компании состоит только из цифр

def test_add_employer(get_token): #Проверки с новым сотрудником
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
  "id": 0,
  "firstName": "Ivan",
  "lastName": "Ivanov",
  "middleName": "",
  "companyId": com_id,
  "email": "test@mail.ru",
  "url": "string",
  "phone": "string",
  "birthdate": "2024-06-24T13:04:28.829Z",
  "isActive": 'true'
}
    new_employer_id = (employer.add_new(token, body_employer))['id']
    assert new_employer_id is not None #Проверяю, что id нового сотрудника не пустое
    assert str(new_employer_id).isdigit() #Проверяю, что id нового сотрудника состоит из цифр
    info = employer.get_info(new_employer_id) #Получаю информацию о новом сотруднике
    assert info.json()['id'] == new_employer_id #Проверяю, что id нового сотрудника соответсвует id при его создании
    assert info.status_code == 200 #Проверяю, что код ответа = 200

def test_add_employer_without_token(): #Проверяю, что невозможно создать сотрудника без токена
    com_id = company.last_active_company_id()
    token = ""
    body_employer = {
  "id": 0,
  "firstName": "Ivan",
  "lastName": "Ivanov",
  "middleName": "",
  "companyId": com_id,
  "email": "test@mail.ru",
  "url": "string",
  "phone": "string",
  "birthdate": "2024-06-24T13:04:28.829Z",
  "isActive": 'true'
}
    new_employer = employer.add_new(token, body_employer)
    assert new_employer['message'] == 'Unauthorized' 

def test_add_employer_without_body(get_token): #Проверяю, что при отправке запроса на создание сотрудника с пустым телом, в ответе будет ошибка
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {}
    new_employer = employer.add_new(token, body_employer)
    assert new_employer['message'] == 'Internal server error'

def test_get_employer():  #Проверяю, что в ответе на запрос списка сотрудников компании содержится именно список
        com_id = company.last_active_company_id()
        list_employers = employer.get_list(com_id)
        assert isinstance(list_employers, list)

def  test_get_list_employers_missing_company_id(): #Проверяю, что при запросе на получение списка сотрудников, поле "id компании" является обязательным
    try:
          employer.get_list()
    except TypeError as e:
         assert str(e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"

def test_get_list_employers_invalid_company_id(): #Проверяю, что при запросе на получение списка сотрудников, поле "id компании" должно быть валидным
    try:
          employer.get_list('')
    except TypeError as e:
         assert str(e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"

def test_get_info_new_employers_missing_eployer_id(): #Проверяю, что при запросе на получение информации о сотрудниках, поле "id сотрудника" должно быть обязательным
    try:
          employer.get_info()
    except TypeError as e:
         assert str(e) == "Employer.get_info() missing 1 required positional argument: 'employee_id'"

def test_change_employer_info(get_token): #Проверки с изменением информации о сотруднике
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
  "id": 0,
  "firstName": "Ivan",
  "lastName": "Ivanov",
  "middleName": "",
  "companyId": com_id,
  "email": "test@mail.ru",
  "url": "string",
  "phone": "string",
  "birthdate": "2024-06-24T13:04:28.829Z",
  "isActive": 'true'
}
    just_employer = employer.add_new(token, body_employer)
    id = just_employer['id']
    body_change_employer = {
  "lastName": "Sidorov",
  "email": "test2@mail.ru",
  "url": "string",
  "phone": "string",
  "isActive": 'true'
    }
    employer_changed = employer.change_info(token, id, body_change_employer)
    assert employer_changed.status_code == 200 #Проверяю, что информация о сотруднике успешно изменена
    assert id == employer_changed.json()['id'] #Проверяю, что у сотрудника не изменилось id
    assert (employer_changed.json()["email"]) == body_change_employer.get("email") #Проверяю, что у сотрудника изменилась почта

def test_employers_missing_in_and_token(): #Проверяю, что поля 'id сотрудника', 'body', 'token' обязательные, в запросе на изменение информации о сотруднике
    try:
          employer.change_info()
    except TypeError as e:
        assert str(e) == "Employer.change_info() missing 3 required positional arguments: 'token', 'employee_id', and 'body'"