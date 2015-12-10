#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

#Path=str(raw_input('Please input the dir_path:'))
Path='/home/hufu/python/python_scripts'

def search(Path):
    for p in os.listdir(Path):
        if os.path.isfile(os.path.join(Path,p)):
            print(os.path.join(Path,p))
        if os.path.isdir(os.path.join(Path,p)):
            search(os.path.join(Path,p))


search(Path)
