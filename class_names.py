# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 00:40:20 2020

@author: Boaz
"""

import os


with open("class.txt", 'a') as f:
    for c in os.listdir(): 
        if not (c.endswith('.txt') or c.endswith('.py')):
            f.write(c + "\n")
    