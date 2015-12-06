#!/usr/bin/env python
# -*- coding: UTF-8 -*-
n=int(raw_input('Plesea input a number:'))
l=list(range(1,n+1))
def f(x,y):
    return str(x)+str(y)
print(reduce(f,l))
