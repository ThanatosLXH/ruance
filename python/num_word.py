#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 21:42
# @Author  : LXH
# @File    : num_word.py

conv = {
    'a': 2,
    'b': 2,
    'c': 2,
    'd': 3,
    'e': 3,
    'f': 3,
    'g': 4,
    'h': 4,
    'i': 4,
    'j': 5
}

word = input('请输入单词：')
print('对应的数字为:', end='')
for i in word:
    print(conv[i], end='')