#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/19 16:26
# @Author  : zc
# @File    : base_page.py

from common.driver import Driver


class Page(object):
    safe_url = "https://fms.17mine.net/#/login?redirect=%2Fdashboard"

    # def __init__(self,webdriver = Driver().driver(), baseUrl = safe_url):
    def __init__(self,webdriver, baseUrl = safe_url):

        self.driver = webdriver
        self.baseUrl = baseUrl
        self.timeout = 10


    def on_open(self):
        return self.driver.current_url == self.baseUrl + self.url


    def open(self):
        self._open(self.url)


    def _open(self,url):
        url = self.baseUrl + url
        self.driver.get(url)
        assert self.on_open(),"url is error :%s" %url


    def find_element(self,*loc):
        return self.driver.find_element(*loc)


    def send_keys(self,loc,text):
        self.find_element(*loc).send_keys(text)


    def click(self,loc):
        self.find_element(*loc).click()


    def getText(self,loc):
        return self.find_element(*loc).text