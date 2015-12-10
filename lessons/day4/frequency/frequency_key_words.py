#!/usr/bin/env python
# -*- coding: UTF-8 -*-
l=['Dream', 'I', 'a', 'do', 'have', 'have', 'one', 'you']
def tj(l):
    l0=[]
    for w in l:
        l0.append((w,l.count(w)))
    print(set(l0))

tj(l)