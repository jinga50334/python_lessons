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
#d=dict()
#for i in range(1,5):
#    for j in range(10,14):
#        pass
#    if i==2:
#        print('i=1')
#        print(d)
#        continue #表示跳过该次循环继续下面的循环，该次循环结果不记录。
#    d['#',i]=i+1
#    if i==3:
#        break
#
#print('mark')
#print(d)
###########################
#while  1:
#    print('hello world')
#    x = str(raw_input('Please input (STOP/stop) to stop this while:'))
#    if x == 'stop' or x == 'STOP':
#        break
###########################
#x = str(raw_input('Please input start to start this while:'))
#while x == 'start' or x == 'START':
#    print('while')
###########################
x = str(raw_input('Please input start to start this while:'))
while x == 'start' or x == 'START':
    print('while')
    if not x: #表示如果满足x没有任何输入（比如直接回车）则执行以下命令
        break
