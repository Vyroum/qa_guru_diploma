import allure
from pages.api.login_api_steps import LoginAPI
from pages.web_ui.login import Login




api_login = LoginAPI()
login_action = Login()

@allure.tag("api")
@allure.title("Проверка успешной аутентификации через API")
def test_api_successful_authentication():
    api_login.successful_authentication_through_api()
    api_login.check_successful_authorization_in_browser()


@allure.tag("api")
@allure.title("Проверка аутентификации с ошибкой через API")
def test_api_failed_authentication():
    api_login.failed_authorization_through_api()


@allure.tag("api")
@allure.title("Проверка логаута через API")
def test_logout_api():
    api_login.successful_authentication_through_api()
    api_login.logout_through_api()
    login_action.check_successful_logout()
