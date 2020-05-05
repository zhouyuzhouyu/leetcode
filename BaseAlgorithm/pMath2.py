"""
计数质数
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        listAll = [True for i in range(n)]
        for i in range(2,n):
            if listAll[2]:
                j = 2
                while i * j < n:
                    listAll[i*j] = False
                    j += 1

        return listAll.count(True) - 2



