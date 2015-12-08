#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

Path=str(raw_input('Please input the dir_path:'))

def search(Path):
    for p in os.listdir(Path):
        if os.path.isfile(os.path.join(Path,p)):
            print(os.path.join(Path,p))
        else:
            search(p)

search(Path)
