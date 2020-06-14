#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# handle层调用page层
from page.register_page import RegisterPage
from Util.get_code import GetCode
class RegisterHandle:
    def __init__(self, driver):
        self.driver = driver
        self.re_page = RegisterPage(self.driver)
    # 输入邮箱
    def send_user_email(self, email):
        return self.re_page.get_email_element().send_keys(email)

        # 输入用户名
    def send_user_name(self, username):
       return self.re_page.get_name_element().send_keys(username)

        # 输入密码
    def send_user_pwd(self, pwd):
       return self.re_page.get_pwd_element().send_keys(pwd)

        # 输入验证码
    def send_user_code(self, code):
        # get_code_text = GetCode(self.driver)
        # code = get_code_text.get_code_image(file_code)
        return self.re_page.get_code_element().send_keys(code)

    #获取文字信息，输入 不同的错误信息，提示语不同，，用户名错误，密码错误。。。。
    def get_user_text(self, info):
        text = ''
        try:
            if info == 'user_email_error':
                text = self.re_page.get_email_error_element().text
            elif info == 'user_name_error':
                text = self.re_page.get_name_error_element().text
            elif info == 'pwd_error':
                text = self.re_page.get_pwd_error_element().text
            elif info == 'code_error':
                text = self.re_page.get_code_error_element().text

        except:
            text = None
        # print(text)
        return text

#     点击注册按钮
    def click_register_button(self):
       self.re_page.get_button_element().click()

#         获取注册按钮文字
    def get_register_text(self):
        return self.re_page.get_button_element().text


# re_handle = RegisterHandle()