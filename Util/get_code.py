#!/user/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
from Util.ShowapiRequest import ShowapiRequest
from Util.read_image import base64_api
import time
class GetCode:
	def __init__(self, driver):
		self.driver = driver
	# 获取图片
	def get_code_image(self, file_name) :
		self.driver.save_screenshot(file_name)
		code_element = self.driver.find_element_by_id("getcode_num")
		left = code_element.location['x']
		top = code_element.location['y']
		right = code_element.size['width'] + left
		height = code_element.size['height'] + top
		# 打开图片创建一个对象
		im = Image.open(file_name)
		# 裁剪图片
		img = im.crop((left, top, right, height))
		img.save(file_name)
		time.sleep(3)
		img_path = file_name
		img = Image.open(img_path)
		result = base64_api(uname='Olivia_Liu', pwd='!nrmdl2003', img=img, typeid=11)
		time.sleep(2)
		return result