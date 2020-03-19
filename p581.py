#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 6:48
# @Author  : yu.zhou
# @Email   : 524112470@qq.com
# @File    : p581.py
# @Software: PyCharm

"""
581. 最短无序连续子数组
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
"""


class Solution:
    def findUnsortedSubarray(self, nums: [int]) -> int:
        nums2 = sorted(nums)
        lI = len(nums) - 1
        rI = 0
        for i in range(len(nums)):
            if nums[i] != nums2[i]:
                lI = min(lI, i)
                rI = max(i, rI)

        return rI - lI + 1 if rI - lI > 0 else 0


print(Solution().findUnsortedSubarray([2,6,4,8,10,9,15]))