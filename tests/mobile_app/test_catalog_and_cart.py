from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, by


def test_find_item_in_catalog():
    with step("Пропуск стартовой страницы"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/textViewSkip")).click()

    with step("Отмена геолокации геолокации"):
        browser.element((AppiumBy.ID, "com.android.packageinstaller:id/permission_deny_button")).click()

    with step("Подтвеждение отмены геолокации"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/buttonCancel")).click()

    with step("Ввод города"):
        browser.element(by.text("Москва")).click()

    with step("Закрытие обучающей подсказки"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/buttonClose")).click()

    with step("Поиск товара в каталоге"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/editTextSearch")).type("Пылесос")
        browser.element(by.text("Пылесосы для дома")).click()
    with step("Подтверждение успешного поиска категории 'Пылесосы для дома'"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/textViewCategoryName")).should(have.text("Пылесосы для дома"))

    with step("Добавление предмета в корзину"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/buttonPrimaryAction")).click()

    with step("Открытие корзины"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/buttonGoToCart")).click()

    with step("Проверка того что предмет добавлен в корзину"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/textViewName")).should(have.text("Пылесос"))

    with step("Удаление предмета из корзины"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/textViewDeleteSelected")).click()

    with step("Проверка удаления из корзины"):
        browser.element((AppiumBy.ID, "com.notissimus.allinstruments.android:id/viewBackground")).should(not have.text("Пылесос"))



