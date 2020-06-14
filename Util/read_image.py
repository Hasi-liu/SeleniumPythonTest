#!/user/bin/env python3
# -*- coding: utf-8 -*-
# coding:unicode_escape
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
from PIL import Image
import json
import requests
import base64
from io import BytesIO
from sys import version_info

# pytesseract只能识别比较规整的验证码
# image = Image.open("D:/test01.png")
# text = pytesseract.image_to_string(image)
# print(text)
#
'''
r = ShowapiRequest("http://route.showapi.com/932-5", "254178", "d99706819aab48dba5422fa058cd41dc")
r.addBodyPara("type", "1")
r.addBodyPara("secure", "false")
r.addFilePara("image", "D:/test01.png")
res = r.post()
print(res.text)
'''

def base64_api(uname, pwd,  img, typeid):
    img = img.convert('RGB')
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    if version_info.major >= 3:
        b64 = str(base64.b64encode(buffered.getvalue()), encoding='utf-8')
    else:
        b64 = str(base64.b64encode(buffered.getvalue()))
    data = {"username": uname, "password": pwd, "image": b64, "typeid":typeid}
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


if __name__ == "__main__":
    img_path = "D:/test01.png"
    img = Image.open(img_path)
    result = base64_api(uname='Olivia_Liu', pwd='!nrmdl2003', img=img, typeid=11)
    print(result)