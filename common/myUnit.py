#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/09 17:58
# @Author  : zc
# @File    : myUnit.py

import unittest
from common.driver import Driver

class Mytest(unittest.TestCase):

    def setUp(self):

        print("start")
        self.driver = Driver().driver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def tearDown(self):
        print("stop")
        pass