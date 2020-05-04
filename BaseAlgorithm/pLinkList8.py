"""
二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。



示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        result = {}

        def __levelOrder(leftN: TreeNode, rightN: TreeNode, level: int):
            if leftN:
                if level in result:
                    result[level].append(leftN.val)
                else:
                    result[level] = [leftN.val]

                __levelOrder(leftN.left, leftN.right, level + 1)
            if rightN:
                if level in result:
                    result[level].append(rightN.val)
                else:
                    result[level] = [rightN.val]

                __levelOrder(rightN.left, rightN.right, level + 1)

        if root:
            result[0] = [root.val]
        else:
            return []

        __levelOrder(root.left, root.right, 1)

        i = 0
        resultL = []
        while i in result:
            resultL.append(result[i])
            i += 1

        return resultL







