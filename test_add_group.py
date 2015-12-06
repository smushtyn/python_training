# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture #-------------------------------#указывает для pytest, что функция создает именно фикстуру
                                                #(@ превращает функцию в инициализатор фикстуры)
def app(request):#------------------------------#функция инициализации фикстуры
    fixture = Application()#--------------------#создана фикстура - обьект типа Application
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="sdfsdfs", header="dfgasdf", footer="sdfasfgas"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group( Group(name="", header="", footer=""))
    app.logout()