"""
46. 全排列
难度
中等

706

收藏

分享
切换为英文
关注
反馈
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            numsT = nums.copy()
            numsT.pop(i)
            resultOther = self.permute(numsT)

            if not resultOther:
                result.append([nums[i]])
            else:
                for lOther in resultOther:
                    result.append([nums[i]] + lOther)

        return result


print(Solution().permute([1,2,3]))



