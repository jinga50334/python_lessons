#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#打印倒三角
n=int(input('Please input the num:'))
for i in range(-n,0):
    print(' '*(n-abs(i))),(' *')*abs(i)
