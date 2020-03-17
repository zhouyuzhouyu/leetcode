#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 0:43
# @Author  : yu.zhou
# @Email   : 524112470@qq.com
# @File    : p53.py
# @Software: PyCharm

'''
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
'''


class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum


print(Solution().maxSubArray([1]))











