#!/usr/bin/env python
# -*- coding: UTF-8 -*-
n=int(raw_input('Please input the number:'))
def f(n):
        if n==1:
            return 1
        return n*f(n-1)
print(f(n))

