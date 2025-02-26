import requests
from selene import browser
import allure
from dotenv import load_dotenv
import os
from jsonschema import validate

from pages.web_ui.login import Login
from resources.schema import login_schema
from allure_commons.types import AttachmentType
import project

login_action = Login()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
}


class LoginAPI:

    def successful_authentication_through_api(self):
        with allure.step('Запрос на авторизацию с валидными данными'):
            load_dotenv()
            email = os.getenv('EMAIL')
            password = os.getenv('PASSWORD')
            r = requests.post(f'{project.config.base_url}api/site/login/', data={"login": email, "password": password},
                              allow_redirects=False, headers=headers)
        with allure.step("Проверка статус кода"):
            assert r.status_code == 200
            body = r.json()
        with allure.step("Валидация JSON-схемы ответа"):
            validate(body, login_schema)

        with allure.step("Получение cookie из API"):
            cookie = r.cookies.get("site_laravel_session")

        with allure.step("Добавление cookie из API в сессию браузера"):
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
            allure.attach(body=str(r.status_code), name="Status Code", attachment_type=AttachmentType.TEXT,
                          extension="txt")

    def check_successful_authorization_in_browser(self):
        with allure.step("Проверка успешной авторизации в браузере"):
            login_action.close_tutorial_window()
            login_action.open_login_form_or_user_page()
            login_action.check_successul_authorization()

    def failed_authorization_through_api(self):
        with allure.step("Запрос на авторизацию с невалидными данными"):
            r = requests.post(f'{project.config.base_url}api/site/login/',
                              data={"login": "1231@awfwa.ru", "password": "awgagawg"}, allow_redirects=False)
        with allure.step("Проверка статус кода"):
            assert r.status_code == 401
            allure.attach(body=r.url, name="Request URL", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=r.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=str(r.status_code), name="Status Code", attachment_type=AttachmentType.TEXT,
                          extension="txt")

    def logout_through_api(self):
        with allure.step("Запрос на логаут через API"):
            r = requests.get(f'{project.config.base_url}profile/logout', data={"login": email, "password": password},
                             allow_redirects=False, headers=headers)
        with allure.step("Проверка статус кода"):
            assert r.status_code == 302
            allure.attach(body=r.url, name="Request URL", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=r.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=str(r.status_code), name="Status Code", attachment_type=AttachmentType.TEXT,
                          extension="txt")

        with allure.step("Получение cookie из API"):
            cookie = r.cookies.get("site_laravel_session")

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
