#!/usr/bin/env python
# -*- coding: UTF-8 -*-
c=1
cnt=0
for i in range(1,121,1):
    c=c*i
print(c)
d=c
s=len(str(d))
for i in range(1,s):
    cnt=d%(10**i)
    if cnt==0:
        cnt=cnt+i
        print(cnt)
