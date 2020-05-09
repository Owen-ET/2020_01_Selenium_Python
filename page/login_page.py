#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/27 15:27
# @Author  : zc
# @File    : login_page.py

from page.base_page import Page
from selenium.webdriver.common.by import By
# from common.driver import driver
from common.getVerification import GetVerification
from time import sleep


class Login(Page):


    url = ''


    # 用户名
    username_loc = (By.NAME,"telephone")
    # 密码
    password_loc = (By.NAME,"password")
    # 验证码
    verification_loc = (By.NAME,"verification")
    # 登录按钮
    loginBtn_loc = (By.CSS_SELECTOR,".loginbtn")
    # 错误提示
    errorMsg_loc = (By.CSS_SELECTOR,".el-message__content")



    def input_username(self,username):
        '''输入用户名'''
        self.send_keys(self.username_loc,username)


    def input_password(self,password):
        '''输入用户名'''
        self.send_keys(self.password_loc,password)


    def input_verification(self,verification):
        '''输入验证码'''
        self.send_keys(self.verification_loc,verification)


    def click_loginBtn(self):
        '''点击登录按钮'''
        self.click(self.loginBtn_loc)


    def getErrorMsg(self):
        '''获取错误提示'''
        return self.getText(self.errorMsg_loc)


    def getVerification(self):
        ''''''


    def login_action(self,username,password,verification):
        '''登录资金管理系统'''
        self.open()
        self.input_username(username)
        self.input_password(password)
        self.input_verification(verification)
        self.click_loginBtn()
        sleep(0.5)
        print(self.getErrorMsg())


# if __name__ == '__main__':
#     Login().login_action(
#         username="13752752585",
#         password="123456",
#         verification="1234"
#     )