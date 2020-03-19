#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 4:33
# @Author  : yu.zhou
# @Email   : 524112470@qq.com
# @File    : convertListToTree.py
# @Software: PyCharm

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def convertListToTree(listA: list) -> TreeNode:
    if not listA:
        return None

    return listCreateTree(None, listA, 0)


def listCreateTree(root: TreeNode, llist: list, i: int):
    if i < len(llist):
        if not llist[i]:
            return None
        else:
            root = TreeNode(llist[i])
            root.left = listCreateTree(root.left, llist, 2 * i + 1)
            root.right = listCreateTree(root.right, llist, 2 * i + 2)
            return root

    return root


head = convertListToTree(['1','2','3',None,'4','5'])

print(12)