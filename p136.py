#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 4:53
# @Author  : yu.zhou
# @Email   : 524112470@qq.com
# @File    : p136.py
# @Software: PyCharm

"""
136. 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
"""

# class Solution:
#     def singleNumber(self, nums: [int]) -> int:
#         nums.sort()
#         for i in range(0, len(nums), 2):
#             if i+1 >= len(nums):
#                 return nums[i]
#             if nums[i] != nums[i+1]:
#                 return nums[i]

from functools import reduce
from operator import xor

class Solution:
    def singleNumber(self, nums: [int]) -> int:
        return reduce(xor, nums)

