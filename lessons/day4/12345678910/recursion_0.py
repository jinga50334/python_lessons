#!/usr/bin/env python
# -*- coding: UTF-8 -*-
x=int(raw_input('Plesea input a number:'))
def f(x):
    if x==1:
        return 1
    else:
        l=len(str(x))
        return 10**l*f(x-1)+x
print(f(x))
