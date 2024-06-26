import pytest
import requests
from lesson_8.constants import x_client_URL

@pytest.fixture()
def get_token(username = 'stella', password = 'sun-fairy'):
    log_pass = {'username' : username, 'password' : password}
    resp_token = requests.post(x_client_URL + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token