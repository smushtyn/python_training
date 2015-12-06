# -*- coding: utf-8 -*-

# в результате декомпозиции были выделены методы- помощники SessionHelper и GroupHelper, в которые были перенесены
# методы отвечающие за сессию (логин/логаут) и методы отвечающие за создание групп
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import Grouphelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        # конструирование помощника session
        self.session = SessionHelper(self)      # Передаем в помощник ссылку на фикстуру (объект класса Application)
                                                # это дает возможность одному помощнику обратиться к другому помощнику
                                                # через объект класса Application
        self.group = Grouphelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()