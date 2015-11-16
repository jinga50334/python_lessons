#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#1)  1 * 2 * 3 …  120  
#2)  求上述结果的尾部0 的个数。

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
        l=list()
        l.append(cnt)
print('The end 0 total:')
print(l[-1])
