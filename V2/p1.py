#!/usr/bin/python3

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        hashMap = {}

        s = 6
        for index, num in enumerate(nums):
            if hashMap.get(target - num) is not None:
                return [hashMap.get(target - num), index]
            else:
                hashMap[num] = index

