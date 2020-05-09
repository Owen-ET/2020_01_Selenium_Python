#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/09 17:56
# @Author  : zc
# @File    : test_login_case.py

from common.myUnit import Mytest
from page.login_page import Login
import unittest

class TestLoginCase(Mytest):


    def user_login_verify(self,username='',password='',verification=''):
        Login(self.driver).login_action(username,password,verification)


    def test_login1(self):
        self.user_login_verify(
            username="13752752585",
            password="123456",
            verification="12345"
        )
        po = Login(self.driver).getErrorMsg()
        self.assertEqual(po,"验证码不对!",msg="测试用例预期结果不对！")


    def test_login2(self):
        self.user_login_verify(
            username="13752752585",
            password="123456",
            verification="1234"
        )
        po = Login(self.driver).getErrorMsg()
        self.assertEqual(po,"验证码不正确",msg="测试用例预期结果不对！")

# if __name__ == '__main__':
#     unittest.main()
