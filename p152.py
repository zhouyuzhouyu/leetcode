"""
152. 乘积最大子数组
难度
中等

586

收藏

分享
切换为英文
关注
反馈
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。



示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""
from functools import reduce
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return None

        res = nums[0]
        preMax = nums[0]
        preMin = nums[0]
        for i in range(1, len(nums)):
            currMax = max(preMax * nums[i], preMin * nums[i], nums[i])
            currMin = min(preMax * nums[i], preMin * nums[i], nums[i])
            res = max(res, currMax)
            preMax = currMax
            preMin = currMin

        return res


print(Solution().maxProduct([2,3,-2,4]))