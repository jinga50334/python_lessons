#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#1)  1 * 2 * 3 …  120  
#2)  求上述结果的尾部0 的个数。

c=1
for i in range(1,121,1):
    c=c*i
print('The result is:')
print(c)
d=str(c)
s=len(d)
cnt=0
for i in range(1,s):
    if d[-i]=='0':
        cnt=cnt+1
    else:
        break

print('The end 0 total:')
print(cnt)
