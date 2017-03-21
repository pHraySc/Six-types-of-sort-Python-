# -*- coding: utf-8 -*-
'''
Created on 2017年3月7日

@author: admin

#Filename:randata.py  
'''

import random

def getrandomdata(num):
    a = []
    i = 0
    while i < num:
        a.append(random.randint(0, 10000000))
        i += 1
    return a