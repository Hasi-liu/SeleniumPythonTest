#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 根据2017年10月份最新的手机号正则进行编码， 正则如下：
# (13\d|14[579]|15[^4\D]|17[^49\D]|18\d)\d{8}

import random

def create_phone():
    #第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    #第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9)

    }[second]
    # data[key]

    #最后八拉数字
    suffix = random.randint(9999999, 100000000)

    #拼接手机号
    return"1{}{}{}".format(second, third, suffix)

print(create_phone())


