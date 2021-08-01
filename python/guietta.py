#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 20:00
# @Author  : LXH
# @File    : guietta.py

from guietta import  Gui, Quit
gui = Gui(
	[ "Enter numbers:",  "__a__", "+", "__b__", ["Calculate"] ],
	[    "Result: -->", "result",   _,       _,             _ ],
	[                _,        _,   _,       _,          Quit ]
)

with gui.Calculate:
	gui.result = float(gui.a) + float(gui.b)

gui.run()
