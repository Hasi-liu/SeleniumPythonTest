#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
from PIL import Image
import time
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Edge()
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
# for i in range(5):
# 	#通过''.join可以把返回的List转为str
# 	user = ''.join(random.sample('1234567890abcddfg', 5))+'@163.com'
# 	print(user)
driver.get("http://test-tc.zhan.com/login")
driver.maximize_window()
time.sleep(5)
EC.title_contains("LuckyFrame")
driver.execute_script('document.body.style.zoom="0.667"')
driver.save_screenshot("D:/test.png")
code_element = driver.find_element_by_css_selector("#signupForm > div.row.m-t > div:nth-child(2) > a > img")
# print(code_element.location)   {'x': 532, 'y': 338}
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
# 打开图片创建一个对象
im = Image.open("D:/test.png")
# 裁剪图片
img = im.crop((left, top, right, height))
img.save("D:/test01.png")

# # 转为灰度,灰度和亮度不是必须的
# code_img = Image.open("D:/test01.png")
# gray_img = code_img.convert('L')
# #增强亮度
# enhance_img = ImageEnhance.Contrast(gray_img)
# enhance_img = enhance_img.enhance(1)
# enhance_img.save("D:/test01.png")
# enhance_img.show()


# r = ShowapiRequest("http://route.showapi.com/932-5", "254178", "d99706819aab48dba5422fa058cd41dc")
# r.addBodyPara("type", "1")
# r.addBodyPara("secure", "false")
# r.addFilePara("image", "D:/test01.png")
# res = r.post()
# text = res.json()["showapi_res_body"]["check"]
# print(text)
# img_path = "D:/test01.png"
# img = Image.open(img_path)
# result = base64_api(uname='Olivia_Liu', pwd='!nrmdl2003', img=img, typeid=11)
# print(result)






# #不能直接传element，因为ec方法里包含了driver.find，所以只需要传查找方法和定位的值就可以
# # element = driver.find_element_by_class_name("col-xs-6")
# # EC.visibility_of_element_located(element)
# locator = (By.CLASS_NAME, "col-xs-6")
# # EC.presence_of_element_located,就否的dom元素中存在，不一定可见
# e = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locator))
# print(e)


# username = driver.find_element_by_name("username")
# print(username.get_attribute("placeholder"))
# username.send_keys("Olivia.Liu")
# # 获取输入的值
# print(username.get_attribute("value"))


# driver.find_element_by_name("username").send_keys("Olivia.Liu")
# driver.find_element_by_name("password").send_keys("!nrmdl2003")
# # 用classname定位时不能把空格后面的加上form-control pword
# # 当父级有多定的时候默认会定位第一个，如果不想定位第一个可以用find_elements定位第n个[n]
# # el = driver.find_elements_by_class_name("col-xs-6")[0]
# el = driver.find_element_by_class_name("col-xs-6")
# e = el.find_element_by_class_name("form-control")
# e.send_keys("0000")
# #driver.find_element_by_xpath("//*[@id='signupForm']/div[1]/div[1]/input").send_keys("111")



# 验证码解决思路
# 1.因为是内部网站，可以让开发设置一个万能的，或者直接去掉
# 2.如果是登录有验证码，可以以cookie的形式存在，把验证码绕过，也就说
# 有一个登录状态，只要用cookie注入，让账号保持在登录状态
# 3.识别验证码

driver.close()

