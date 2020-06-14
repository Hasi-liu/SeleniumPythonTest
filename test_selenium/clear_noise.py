#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from PIL import Image
def clear_noise(img):
    noise_img = Image.open(img)
    # 获取图片尺寸
    w, h = noise_img.size
    for y in range(w, h-1):
        for x in range(1, w-1):
            count = 0
            if noise_img[x, y-1] > 245:
                count = count +1
            if noise_img[x, y+1] > 245:
                count = count + 1
            if noise_img[x - 1, y] > 245:

                count = count + 1

            if noise_img[x + 1, y] > 245:

                count = count + 1

            if noise_img[x - 1, y - 1] > 245:

                count = count + 1

            if noise_img[x - 1, y + 1] > 245:

                count = count + 1

            if noise_img[x + 1, y - 1] > 245:

                count = count + 1

            if noise_img[x + 1, y + 1] > 245:

                count = count + 1

            if count > 4:

                noise_img[x, y] = 255
    return noise_img

if __name__ == '__main__':
    img = 'D:/test01.png'
    clear_noise(img).show()