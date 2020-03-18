#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 7:55
# @Author  : yu.zhou
# @Email   : 524112470@qq.com
# @File    : p198.py.py
# @Software: PyCharm

"""
198. 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

class Solution:
    def rob(self, nums: List[int]) -> int:
"""

class Solution:
    def rob(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0

        # 子问题：
        # f(k) = 偷 [0..k) 房间中的最大金额

        # f(0) = 0
        # f(1) = nums[0]
        # f(k) = max{ rob(k-1), nums[k-1] + rob(k-2) }

        N = len(nums)
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for k in range(2, N + 1):
            dp[k] = max(dp[k - 1], nums[k - 1] + dp[k - 2])
        return dp[N]





print(Solution().rob([1,2,1,1]))