"""
240. 搜索二维矩阵 II
难度
中等

309

收藏

分享
切换为英文
关注
反馈
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        rows = len(matrix)
        colums = len(matrix[0])

        for i in range(rows):
            if matrix[i][0] <= target <= matrix[i][colums - 1]:
                l = 0
                r = colums - 1
                while l <= r:
                    center = (l + r) // 2
                    if matrix[i][center] > target:
                        r = center - 1
                    elif matrix[i][center] < target:
                        l = center + 1
                    else:
                        return True


        return False

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print(Solution().searchMatrix(matrix, 5))