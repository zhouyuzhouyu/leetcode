#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 3:23
# @Author  : yu.zhou
# @Email   : 524112470@qq.com
# @File    : p101.py
# @Software: PyCharm

'''
101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: TreeNode, right: TreeNode):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False

        return (left.val == right.val) and (self.isMirror(left.left, right.right)) \
               and (self.isMirror(left.right, right.left))


