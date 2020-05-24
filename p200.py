"""
200. 岛屿数量
难度
中等

574

收藏

分享
切换为英文
关注
反馈
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。



示例 1:

输入:
11110
11010
11000
00000
输出: 1
示例 2:

输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
"""
from typing import List





class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        def __dfs(r, c):
            grid[r][c] = 0
            for x, y in [(r-1, c), (r+1, c), (r, c+1), (r, c-1)]:
                if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                    __dfs(x, y)



        result = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    result += 1
                    __dfs(r, c)

        return result



