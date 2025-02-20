import time

from selene import browser, be, by


def test_authorization():
    browser.open('/')
    browser.element(by.text("Войти")).click().type("vyroud@gmail.com")
    time.sleep(2)