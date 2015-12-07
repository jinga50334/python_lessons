#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

Path=str(raw_input('Plesea input the path:'))
def Search(Path):
    for p in os.listdir(Path):
        if os.path.isdir(p):
            Search(Path)
        else:
            return p

    print(p)

