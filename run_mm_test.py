#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/09 18:13
# @Author  : zc
# @File    : run_mm_test.py


import os
import time
import unittest
from BSTestRunner import BSTestRunner

if __name__ == '__main__':


    # 当前路径
    base_path = os.path.dirname(os.path.abspath(__file__))
    # 测试用例路径
    testcase_path = base_path + "/test_case/"

    now = time.strftime("%Y-%m-%d %H:%M:%S")
    # 报告路径
    report_path = base_path + "/test_report/" + now + "_report.html"


    fp = open(report_path,'wb')

    runner = BSTestRunner(stream=fp,title="自动化测试报告",description="执行下面用例：")

    discover = unittest.defaultTestLoader.discover(testcase_path,pattern="test*.py")

    runner.run(discover)

    fp.close()