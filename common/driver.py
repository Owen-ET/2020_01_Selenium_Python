#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/19 16:26
# @Author  : zc
# @File    : driver.py

from selenium import webdriver

class Driver(object):

    def driver(self):
        return webdriver.Chrome("/Users/zhangc/Desktop/GitTest/2020Project/Python/MoneyManagement/common/chromedriver")






# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s*%s=%s" %(j,i,j*i),end="   ")
#         # print(str(j)+ "*" +str(i)+"="+str(i*j),end="    ")
#     print("\n")