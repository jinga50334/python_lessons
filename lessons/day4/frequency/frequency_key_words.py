#!/usr/bin/env python
# -*- coding: UTF-8 -*-
l=['Dream', 'I', 'a', 'do', 'have', 'have', 'one', 'you']
def tj(l):
    lnew=list()
    for w in l:
        lnew.append(w,l.count(w))
        if 'w,l.count(w)' not in lnew:
            print(w,l.count(w))

tj(l)