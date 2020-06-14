#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
from selenium import webdriver
from test_selenium.read_image import base64_api
import time
import random
from PIL import Image
from base.find_element import FindElement


class RegisterFunction():
    def __init__(self, url):
        self.driver = self.get_driver(url)

    #获取driver并打开url
    def get_driver(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    #输入用户信息
    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    #定位用户信息，获取element
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取随机数
    def get_rang_user(self):
        user_info = ''.join(random.sample('1234567890abcdefg', 8))
        return user_info

    # 获取图片code
    def get_code_image(self, file_name):
        # self.driver.execute_script('document.body.style.zoom="0.667"')
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_img")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        # 打开图片创建一个对象
        im = Image.open(file_name)
        # 裁剪图片
        img = im.crop((left, top, right, height))
        img.save(file_name)
        img_path = file_name
        img = Image.open(img_path)
        result = base64_api(uname='Olivia_Liu', pwd='!nrmdl2003', img=img, typeid=11)
        return result

    def main(self):
        user_name_info = self.get_rang_user()
        user_email = user_name_info + '@163.com'
        file_name = 'D:/test02.png'
        # code_text = self.get_code_image(file_name)
        self.send_user_info("user_name", user_email)
        time.sleep(2)
        self.send_user_info("password", user_name_info)
        time.sleep(2)
        self.send_user_info("code_text", "111")
        time.sleep(3)
        el = self.get_user_element("register_button")
        # 调用js
        self.driver.execute_script("arguments[0].click();", el)
        time.sleep(2)

        # ele_id = "layui-layer13"
        # param = (By.ID, ele_id)
        # 元素可见时，再进行后续操作
        # print(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(param)))
        # 等待alert弹出框可见
        # WebDriverWait(self.driver, 10).until(EC.alert_is_present())

        # # 从html页面切换到alert弹框
        # alert = self.driver.switch_to.alert
        # # 获取alert的文本内容
        # print(alert.text)

        error_img_code = 'document.getElementById("layui-layer13")'
        error_info_code = 'document.getElementById("layui-layer14")'

        # self.driver.execute_script(error_code)
        if error_img_code or error_info_code:
            self.driver.save_screenshot('D:/error_code.png')

        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    register = RegisterFunction('http://test-tc.zhan.com/login')
    register.main()

#     多个浏览器依次跑和同时跑2-24

