#!/usr/bin/env python
# -*- coding: UTF-8 -*-
n=int(raw_input('Please input the number:'))
def fun(n):
        if n==1:
            return 1
        else:
            for i in range(1,n):
                fun(n)*

fun(n)

