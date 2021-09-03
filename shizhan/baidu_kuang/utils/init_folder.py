#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/9/3 19:41
# @Author  : LXH
# @File    : init_folder.py

import os

def init_html_folder(date):
    html_path = './../report/html/'
    folder_path = html_path + date
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    png_path = './../report/png/'
    folder_path = png_path + date
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    log_path = './../report/log/'
    folder_path = png_path + date
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)