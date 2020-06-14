#!/user/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from test_selenium.read_image import base64_api
import time
import random
from PIL import Image
driver = webdriver.Chrome()

# 浏览器初始化
def driver_init():
	driver.get("http://test-tc.zhan.com/login")
	driver.maximize_window()
	time.sleep(5)
# 获取element信息
def get_element_name(name):
	element = driver.find_element_by_name(name)
	return element
def get_element_id(id):
	element = driver.find_element_by_name(id)
	return element

#获取随机数
def get_rang_user():
	user_info = ''.join(random.sample('1234567890abcdefg', 8))
	return user_info

# 获取图片
def get_code_image(file_name):
	driver.save_screenshot(file_name)
	code_element = driver.find_element_by_css_selector("#signupForm > div.row.m-t > div:nth-child(2) > a > img")
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

# 运行主程序
def run_main():
	user_name_info = get_rang_user()
	user_email = user_name_info + '@163.com'
	file_name = 'D:/test02.png'
	driver_init()
	get_element_name("username").send_keys(user_name_info)
	get_element_name("password").send_keys(user_email)
	text = get_code_image(file_name)
	get_element_name("validateCode").send_keys(text)
	get_element_id("btnSubmit").click()
	driver.close()

run_main()
