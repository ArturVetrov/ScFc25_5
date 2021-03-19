import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_PetFriends():
    pytest.driver = webdriver.Chrome('/Users/arturvetrov/PycharmProjects/25_5_1/chromedriver')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('Test12345@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на кнопку мои питомцы
    pytest.driver.find_element_by_class_name('nav-link').click()
    #Создаем переменные, и даем значения
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')
    amount = pytest.driver.find_elements_by_xpath('//div[@class=".col-sm-4 left"][1]')
    #Проверки
    for i in range(len(names)):
        #Путь изображения не пуст
        assert images[i].get_attribute('src') != ''
        #Имя не пустое
        assert names[i].text != ''
        #Вид и возраст
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
        #Присутсвтуют все питомцы
        assert amount == len(names)
        #У половины есть фото
        assert len(images) / amount > 0.5
        # У всех питомцев есть имя, возраст и порода
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i].text
        # У всех питомцев разные имена
        assert len(names) == len(set(names))








#python3 -m pytest -v --driver Chrome --driver-path /Users/arturvetrov/PycharmProjects/25_5_1/chromedriver 25_3_1test.py