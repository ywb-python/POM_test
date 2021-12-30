#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/30 21:07
# @Author  : ywb
# @Site    : 
# @File    : baidu_show.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from base.base_page import BasePage

class BaiduShow(BasePage):

    # 页面元素定位
    search_input = (By.ID, 'kw')
    search_button = (By.ID, 'su')

    # 页面元素对象
    def get_input_obj(self):
        ele = self.locate_clc(*BaiduShow.search_input)
        return ele

    def get_button_obj(self):
        ele = self.locate_clc(*BaiduShow.search_button)
        return ele

    # 页面动作
    def search(self):
        self.get_input_obj().send_keys(["python"])
        self.get_button_obj().submit()
