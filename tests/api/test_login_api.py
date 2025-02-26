import requests
from selene import browser, have, be
import allure
from dotenv import load_dotenv
import os
from jsonschema import validate

from pages.web_ui.login import Login
from pages.api.login_api_steps import LoginAPI
from tests.api.schema import login_schema
from allure_commons.types import AttachmentType
import project

login_action = Login()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

api_login = LoginAPI()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
}


@allure.tag("api")
@allure.title("Проверка успешной аутентификации через API")
def test_api_successful_authentication():
   api_login.successful_authentication_through_api
   api_login.check_successful_authorization_in_browser

@allure.tag("api")
@allure.title("Проверка аутентификации с ошибкой через API")
def test_api_failed_authentication():
    api_login.failed_authorization_through_api
 
@allure.tag("api")
@allure.title("Проверка логаута через API")
def test_logout_api():
   api_login.successful_authentication_through_api
   api_login.logout_through_api
   login_action.check_successful_logout()
