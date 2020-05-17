"""
56. 合并区间
难度
中等

423

收藏

分享
切换为英文
关注
反馈
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort(key=(lambda x: x[0]))


        result = []

        currentR = None
        for data in intervals:
            if not currentR:
                currentR = data
            else:
                if data[0] > currentR[1]:
                    result.append(currentR)
                    currentR = data
                else:
                    currentR = [currentR[0],max(currentR[1],data[1])]

        if currentR:
            result.append(currentR)

        return result




print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
