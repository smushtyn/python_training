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
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def change_field_name(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_name("group_name", group.name)
        self.change_field_name("group_header", group.header)
        self.change_field_name("group_footer", group.footer)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page(wd)
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page(wd)
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        #fill group info
        self.fill_group_form(new_group_data)
        #submit changes
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
