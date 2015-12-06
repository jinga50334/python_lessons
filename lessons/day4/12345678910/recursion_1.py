#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#unlimite
s0=int(raw_input('Plesea input a number:'))
def f(x):
    s=0
    for i in range(1,x+1):
        l=len(str(i))
        s=10**l*s+i
    print(s)
f(s0)
