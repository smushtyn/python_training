# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture #-------------------------------#указывает для pytest, что функция создает именно фикстуру
                                                #(@ превращает метод/функцию в инициализатор фикстуры)
def app(request):#------------------------------#функция инициализации фикстуры
    fixture = Application()#--------------------#создана фикстура - обьект типа Application
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="sdfsdfs", header="dfgasdf", footer="sdfasfgas"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()