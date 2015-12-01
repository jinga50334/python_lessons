#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#unlimite
x=int(raw_input('Plesea input a number:'))
def f(x):
    s=0
    for i in range(1,x+1):
        l=len(str(i))
        s=10**l*s+i
    return s
print(f(x))
