#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 2:27
# @Author  : yu.zhou
# @Email   : 524112470@qq.com
# @File    : p226.py
# @Software: PyCharm

"""
226. 翻转二叉树
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invert_tree(root)
        return root

    def invert_tree(self, root: TreeNode):
        if not root:
            return

        root.left, root.right = root.right, root.left
        self.invert_tree(root.left)
        self.invert_tree(root.right)