#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 19:52
# @Author  : LXH
# @File    : Pillow.py

from PIL import Image
# 打开 jpg 图像文件
im = Image.open('reg.png')
# 转换成黑白图像
grayscale = tatras.convert('L')
# 展示图像
grayscale.show()