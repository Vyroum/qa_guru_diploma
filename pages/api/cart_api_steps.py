import requests
from selene import browser
import allure
from jsonschema import validate

from pages.web_ui.cart_page import Cart
from resources.schema import add_to_cart, cart_clear
from resources.cpu import cpu
import project

cart = Cart()

header1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
payload1 = {
    "goods": [
        {
            "good_id": 411819,
            "good_count": 1
        }
    ]
}

class CartAPI:

    def add_item_to_cart_though_api(self):
        with allure.step("Запрос на добавление предмета в корзину"):
            r = requests.put(f'{project.config.base_url}api/site/basket', json=payload1, headers=header1)
            assert r.status_code == 200
            validate(r.json(), add_to_cart)

        with allure.step("Получение куки из API"):
           cookie = r.cookies.get("basket_id")

        with allure.step("Добавление куки из API"):
            browser.open('/')
            browser.driver.add_cookie({
                'name': 'basket_id',
                'value': cookie,
                'domain': 'www.regard.ru',
                 'path': '/',
                'secure': True,
                'httponly': True
                })
            browser.driver.refresh()


    def delete_item_from_cart(self):
        with allure.step("Запрос на добавление предмета в корзину"):
            r = requests.put(f'{project.config.base_url}api/site/basket', json=payload1, headers=header1)
            assert r.status_code == 200
            validate(r.json(), add_to_cart)

        with allure.step("Получение куки из API"):
            cookie = r.cookies.get("basket_id")

        with allure.step("Добавление куки из API"):
                browser.open('/')
                browser.driver.add_cookie({
                'name': 'basket_id',
                'value': cookie,
                'domain': 'www.regard.ru',
                'path': '/',
                'secure': True,
                'httponly': True
            })
                browser.driver.refresh()
        with allure.step("Проверка успешного добавления в корзину"):
            cart.open_cart()
            cart.check_presence_in_cart(cpu)

        with allure.step("Запрос на очистку корзины"):
            r = requests.delete(f'{project.config.base_url}api/site/basket')
            assert r.status_code == 200
            validate(r.json(), cart_clear)

    #Механизм очистки корзины просто очищает куки
    #Поэтому вместо взятие удаленного куки выполняется удаление куки
        with allure.step("Очистка куки корзины"):
            browser.driver.delete_cookie("basket_id")
            browser.driver.refresh()
