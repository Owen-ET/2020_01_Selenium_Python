#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/19 16:13
# @Author  : zc
# @File    : test.py


def add(n,i):
    return n+i

def test():
    for i in range(4):
        yield i+2

g = test()


for n in [7]:
    g = (add(n,i) for i in g)

print(list(g))