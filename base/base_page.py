#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/30 21:03
# @Author  : ywb
# @Site    : 
# @File    : base_page.py
# @Software: PyCharm

from selenium import webdriver


class BasePage:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')

    def locate_clc(self, *args):
        element = self.driver.find_element(*args)
        return element
