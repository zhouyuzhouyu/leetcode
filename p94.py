"""
94. 二叉树的中序遍历
难度
中等

498

收藏

分享
切换为英文
关注
反馈
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stackL = []
        curr = root
        res = []
        while curr or stackL:
            while curr:
                stackL.append(curr)
                curr = curr.left

            curr = stackL.pop()
            res.append(curr.val)
            curr = curr.right

        return res


