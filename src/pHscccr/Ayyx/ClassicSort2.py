# -*- coding: utf-8 -*-
'''
Created on 2017年3月6日

@author: Sccc
'''
import random

def getrandomdata(num):
    a = []
    i = 0
    while i < num:
        a.append(random.randint(0, 10000000))
        i += 1
    return a
# 
# array = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]
# 
# # insert_sort
# for i in range(1, len(array)):
#     if array[i - 1] > array[i]:
#         temp = array[i]  # 当前需要排序的元素
#         index = i  # 用来记录排序元素需要插入的位置
#         while index > 0 and array[index - 1] > temp:
#             array[index] = array[index - 1]  # 把已经排序好的元素后移一位，留下需要插入的位置
#             index -= 1
#         array[index] = temp  # 把需要排序的元素，插入到指定位置
# 
# # print sort result.
# print(array)

def insertSort(arr):  
    for i in range(1, len(arr)):  
        tmp = arr[i] 
        j = i 
        while j > 0 and tmp < arr[j - 1]: 
            arr[j] = arr[j - 1] 
            j -= 1 
        arr[j] = tmp 
'''  
从前往后，先排序前两个元素
把第三个元素插入其中，然后让前三个已经排好序，再把第四个插入前三个中，排好序…以此类推，直到最后一个插入为止
        j = i  
        while j > 0 and arr[j - 1] > arr[i]:  
            j -= 1  
        arr.insert(j, arr[i])
        arr.pop(i + 1) #删除已经完成插入了的元素——>插入后原本的元素i会被往后挤一位。
    return arr 
'''
        
print(insertSort(getrandomdata(5)))
