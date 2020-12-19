# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 02:20:00 2020
@author: Boaz
"""

with open("class.txt", 'r') as f:
  class_names = f.readlines()

for index in range(len(class_names)):
  class_names[index] = class_names[index][:-1]

print(class_names)
