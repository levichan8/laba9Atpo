# test_items.py
import time

def test_add_to_cart_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)  # Задержка для визуальной проверки
    button = browser.find_element("css selector", ".btn-add-to-basket")
    assert button is not None, "Кнопка добавления в корзину не найдена"
