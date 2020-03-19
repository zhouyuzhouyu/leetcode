#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 3:18
# @Author  : yu.zhou
# @Email   : 524112470@qq.com
# @File    : p437.py.py
# @Software: PyCharm

"""
437. 路径总和 III
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, suma: int) -> int:
        if not root:
            return 0
        listAll: [[int]] = []

        if root.left:
            self.makeList(root.left, [root.val], listAll)
        if root.right:
            self.makeList(root.right, [root.val], listAll)

        countAll = 0
        for listA in listAll:
            for i in range(len(listA)):
                for j in range(i+1, len(listA)+1):
                    if sum(listA[i:j]) == suma:
                        countAll += 1

        return countAll






    def makeList(self, root: TreeNode, listA: [int], listAll:[[int]]):
        listA.append(root.val)
        if (not root.left)and (not root.right):
            listAll.append(listA)
            return

        if root.left:
            self.makeList(root.left, listA[:], listAll)

        if root.right:
            self.makeList(root.right, listA[:], listAll)



from convertListToTree import  convertListToTree

c = [10,5,-3,3,2,None,11,3,-2,None,1]
head = convertListToTree(c)
Solution().pathSum(head,8)





