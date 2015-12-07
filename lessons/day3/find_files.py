#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

Path='/home/hufu/python/python_scripts/'
#Keyfile='py'
def search_file(Path):
    os.chdir(Path)
    for p in os.listdir(os.getcwd()):
        if os.path.isfile(p):
            print(os.path.join(os.getcwd(),p))
        else:
            search_file(os.path.join(os.getcwd(),p))
search_file(Path)

