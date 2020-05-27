"""
221. 最大正方形
难度
中等

426

收藏

分享
切换为英文
关注
反馈
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
"""
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    maxSide = max(maxSide, 1)
                    currentMaxSide = min(rows - i, columns - j)
                    for k in range(1, currentMaxSide):
                        flag = True
                        if matrix[i + k][j + k] == '0':
                            break

                        for m in range(k):
                            if matrix[i + k][j + m] == '0' or matrix[i+m][j+k] == '0':
                                flag = False
                                break
                        if flag:
                            maxSide = max(maxSide, k+1)
                        else:
                            break

        return maxSide * maxSide
