#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 6:07
# @Author  : yu.zhou
# @Email   : 524112470@qq.com
# @File    : p461.py
# @Software: PyCharm

"""
461. 汉明距离
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')