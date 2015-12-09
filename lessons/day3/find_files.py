#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

Path=str(raw_input('Please input the dir_path:'))

def search(Path):
    for p in os.listdir(Path):
            print(os.path.join(Path,p))
            if os.path.isdir(os.path.join(Path,p)):
                search(os.path.join(Path,p))


search(Path)
