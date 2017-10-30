# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:23:28 2017

@author: Administrator
"""

#class Solution(object):
#    def twoSum(self, nums, target):
        
nums=[3,2,4]
target=6
if len(nums) <= 1:
    print(' False')
buff_dict = {}
for i in range(len(nums)):
    if nums[i] in buff_dict:
        print( [buff_dict[nums[i]], i])
    else:
        buff_dict[target - nums[i]] = i
#print(Solution.twoSum(1,nums,target))
#self是什么意思？？？
#class是要做什么？
#为何要排序？
#array = [1, 2, 5, 3, 6, 8, 4]
#其实这里的顺序标识是
#[1, 2, 5, 3, 6, 8, 4]
#(0，1，2，3，4，5，6)
#(-7,-6,-5,-4,-3,-2,-1)
#>>>xrange(8)
#xrange(8)
#>>> list(xrange(8))
#[0, 1, 2, 3, 4, 5, 6, 7]生成器