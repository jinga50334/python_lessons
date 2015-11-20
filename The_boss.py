#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys 
reload(sys) 
sys.setdefaultencoding('utf8') 

while True:
    in0=float(raw_input('请输入向老谢申请加薪的数额（可以精确到分）：'))
    if in0>0:
        print('要的也太多了吧，兄弟！O(∩_∩)O~')
    if in0==0:
        print('怎么着也得要点吧！要不就是看不起谢总！')
        continue
    if in0<0:
        print('想加薪？做梦吧，倒贴钱给老谢还差不多！')
        break
