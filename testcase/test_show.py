#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/30 21:16
# @Author  : ywb
# @Site    : 
# @File    : test_show.py
# @Software: PyCharm
import time
import unittest
import warnings

from page.baidu_show import BaiduShow


class TestShow(unittest.TestCase):

    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        print("首页测试")

    def tearDown(self) -> None:
        print("首页测试结束")

    def test_01_search(self):
        BaiduShow().search()
