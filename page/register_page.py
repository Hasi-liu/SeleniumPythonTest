#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from base.find_element import FindElement
class RegisterPage:
    def __init__(self, driver):
        self.find_el = FindElement(driver)

    # 获取邮箱
    def get_email_element(self):
        return self.find_el.get_element('user_email')

        # 获取用户名
    def get_name_element(self):
        return self.find_el.get_element('user_name')

       # 获取密码
    def get_pwd_element(self):
        return self.find_el.get_element('password')

        # 获取code
    def get_code_element(self):
        return self.find_el.get_element('code_text')

#     获取点击button
    def get_button_element(self):
        return self.find_el.get_element("register_button")

    def get_email_error_element(self):
        return self.find_el.get_element("user_email_error")

    def get_name_error_element(self):
        return self.find_el.get_element("user_name_error")

    def get_pwd_error_element(self):
        return self.find_el.get_element("pwd_error")

    def get_code_error_element(self):
        return self.find_el.get_element("code_error")











# re_page = RegisterPage()