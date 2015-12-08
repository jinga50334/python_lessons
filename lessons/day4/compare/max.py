#!/usr/bin/env python
# -*- coding: UTF-8 -*-
Alist=['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10']
n=len(Alist)
def maxlist(n):
    if n==1:
        return Alist[0]
    else:
        return (max(Alist[n-1],Alist[n-2]))
print(maxlist(n))