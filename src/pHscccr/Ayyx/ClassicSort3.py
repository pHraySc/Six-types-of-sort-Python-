# -*- coding: utf-8 -*-
'''
Created on 2017年3月6日

@author: Sccc
'''

from pHscccr.Ayyx.randata import getrandomdata

'''
希尔排序的名称源于它的发明者Donald Shell，该算法是冲破二次时间屏障的第一批算法之一，
不过，直到它最初被发现的若干年后才被证明了它的亚二次时间界。
它通过比较相距一定间隔的元素来工作；各趟比较所用的距离随着算法的进行而减小，
直到只比较相邻元素的最后一趟排序为止。

希尔排序的实质就是分组插入排序，该方法又称缩小增量排序，因DL．Shell于1959年提出而得名。
希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。希尔排序是非稳定排序算法。
希尔排序是基于插入排序的以下两点性质而提出改进方法的：
插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位

先取一个小于n的整数d1作为第一个增量，把文件的全部记录分成d1个组。所有距离为d1的倍数的记录放在同一个组中。先在各组内进行排序；
然后，取第二个增量d2
'''
def shellSort(nums):
    #设定步长
    step = len(nums) / 2
    while step > 0:
        for i in range(step, len(nums)):
            while i >= step and nums[i - step] > nums[i]:
                nums[i - step], nums[i] = nums[i], nums[i - step]
                i -= step
        step /= 2
    return nums

print(shellSort(getrandomdata(5)))



