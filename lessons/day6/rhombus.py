#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#打印菱形
n=int(input('Please input the num:'))
for i in range(1,n):
    print(' '*(n-i)),(' *')*i
for i in range(-n,0):
    print(' '*(n-abs(i))),(' *')*abs(i)
