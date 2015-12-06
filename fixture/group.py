 # -*- coding: utf-8 -*-

class Grouphelper:

    def __init__(self, app):       # конструктор, передаем в качестве параметра ссылку на Application
        self.app = app             # ссылаемся на метод АПП, который в тестах инициализирует фикстуру

    def open_groups_page(self, wd):
        # init group creation
        wd.find_element_by_link_text("Групи").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page(wd)
        wd.find_element_by_name("new").click()
        # fill group info
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
