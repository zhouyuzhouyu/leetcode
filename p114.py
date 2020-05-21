"""
114. 二叉树展开为链表
难度
中等

342

收藏

分享
切换为英文
关注
反馈
给定一个二叉树，原地将它展开为一个单链表。



例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        stack = []
        stack.append(root)
        pre = None
        while stack:
            root = stack.pop()
            if root.right:
                stack.append(root.right)

            if root.left:
                stack.append(root.left)

            if pre:
                pre.right = root
                pre.left = None

            pre = root