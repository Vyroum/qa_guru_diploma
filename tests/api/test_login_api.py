import requests
from selene import browser, have, be
import allure
from dotenv import load_dotenv
import os
from jsonschema import validate, ValidationError
from  tests.api.schema import login
from allure_commons.types import AttachmentType
import project


load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
}

@allure.title("Проверка успешной аутентификации через API")
def test_api_successful_authentication():

    with allure.step('Запрос на авторизацию с валидными данными'):
        email = os.getenv('EMAIL')
        password = os.getenv('PASSWORD')
        r = requests.post(f'{project.base_url}api/site/login/', data={"login": email, "password": password}, allow_redirects=False, headers=headers)
        assert r.status_code == 200
        body = r.json()
        validate(body, login)

    
    with allure.step("Получение cookie из API"):
        cookie = r.cookies.get("site_laravel_session")
        print(cookie)
        
    with allure.step("Добавление cookie из API"):
        browser.open('/')
        browser.driver.add_cookie({
        'name': 'site_laravel_session',
        'value': cookie,
        'domain': '.www.regard.ru',
        'path': '/',
        'secure': True,
        'httponly': True
    })
        browser.driver.refresh()

        allure.attach(body=r.url, name="Request URL", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=r.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(r.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

       
# @allure.title("Проверка аутентификации с ошибкой через API")
# def test_api_unsuccessful_authentication():
#     with allure.step("Запрос на авторизацию с невалидными данными"):
#         r = requests.post('https://www.regard.ru/api/site/login/', data={"login": "1231@awfwa.ru", "password": "awgagawg"}, allow_redirects=False)
#         assert r.status_code == 401

# @allure.title("Проверка логаута через API")
# def test_logout_API():
#     with allure.step('Запрос на авторизацию с валидными данными'):
#         email = os.getenv('EMAIL')
#         password = os.getenv('PASSWORD')
#         r = requests.post('https://www.regard.ru/api/site/login/', data={"login": email, "password": password}, allow_redirects=False)
#         assert r.status_code == 200
#         body = r.json()
#         validate(body, login) 
        
    
