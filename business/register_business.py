#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 也可以把business做为case层
from handle.register_handle import RegisterHandle
import time
class RegisterBusiness:

    def __init__(self, driver):
        self.re_handle = RegisterHandle(driver)

    def user_base(self, email, name, pwd, code):
        self.re_handle.send_user_email(email)
        time.sleep(2)
        self.re_handle.send_user_name(name)
        time.sleep(2)
        self.re_handle.send_user_pwd(pwd)
        time.sleep(2)
        self.re_handle.send_user_code(code)
        time.sleep(2)
        self.re_handle.click_register_button()
        time.sleep(2)


    def register_success(self):
        if self.re_handle.get_register_text() == None:
            return True
        else:
            return False

    #执行操作
    def login_email_error(self, email, name, pwd, file_code):
        self.user_base(email, name, pwd, file_code)
        if self.re_handle.get_user_text('email_error') == None:
            print("邮箱检验不成功")
            return True
        else:
            return False
        #测试first_ddt_case
    def register_function(self, email, username, password, code, assertCode):
        self.user_base(email, username, password, code)
        if self.re_handle.get_user_text (assertCode) == None :
            print("用户名检验不成功")
            return True
        else :
            return False
    #     用户名错误
    def login_name_error(self, email, name, pwd, file_code):
        self.user_base(email, name, pwd, file_code)
        if self.re_handle.get_user_text('name_error') == None:
            print("用户名检验不成功")
            return True
        else:
            return False

        # 密码错误
    def login_pwd_error(self, email, name, pwd, file_code):
        self.user_base(email, name, pwd, file_code)
        if self.re_handle.get_user_text('pwd_error') == None:
            print("密码检验不成功")
            return True
        else:
            return False

            # code错误

    def login_code_error(self, email, name, pwd, file_code):
        self.user_base(email, name, pwd, file_code)
        if self.re_handle.get_user_text('code_error') == None:
            print("验证码检验不成功")
            return True
        else:
            return False














# re_business = RegisterBusiness()