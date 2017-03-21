# -*- coding: utf-8 -*-
'''
Created on 2017年3月6日

@author: Sccc
'''

import random
'''
随机生成0~10000000之间的数值
'''

def getrandomdata(num):
    a = []
    i = 0
    while i < num:
        a.append(random.randint(0,10000000))
        i += 1
    return a

# 1.——冒泡排序——
'''
算法思想：每次从最后开始往前滚，邻接元素两两相比，小元素交换到前面 
第一轮循环把最小的元素上浮至第一个位置，第二小的元素上浮至第二个位置，依次类推 
'''
def bubbleSort(a):  
    l = len(a) - 2
    i = 0  
    while i < l + 1:  
        j = l  
        while j >= i:  
            if(a[j + 1] < a[j]):  
                a[j], a[j + 1] = a[j + 1], a[j]  
            j -= 1  
        i += 1
    return a

print(bubbleSort(getrandomdata(5)))