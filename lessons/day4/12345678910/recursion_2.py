#!/usr/bin/env python
# -*- coding: UTF-8 -*-
n=int(raw_input('Plesea input a number:'))
def f(x,y):
    return str(x)+str(y)
print(reduce(f,range(1,n+1)))
