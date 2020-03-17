#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 3:41
# @Author  : yu.zhou
# @Email   : 524112470@qq.com
# @File    : p104.py
# @Software: PyCharm

"""
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.max_depth(1, root.left),self.max_depth(1, root.right))

    def max_depth(self, n, root: TreeNode):
        if root is None:
            return n
        return max(self.max_depth(n+1, root.left), self.max_depth(n+1, root.right))


