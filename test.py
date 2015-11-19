#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#a=int(raw_input('Please input sth:'))
#l=list()
#for i in range(1,a+1):
#        l.append(i)
#print(l)
#d={'a0':1,'a1':2,'a3':3,'a4':4}
#for x,y in d.items():
#    print(y)
#    print(x)
###########################
d=dict()
for i in range(1,5):
    for j in range(10,14):
        pass
    if i==2:
        print('i=1')
        print(d)
        continue
    d['#',i]=i+1
    if i==3:
        break

print('mark')
print(d)
