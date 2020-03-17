#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 5:13
# @Author  : yu.zhou
# @Email   : 524112470@qq.com
# @File    : p141.py
# @Software: PyCharm

"""
141. 环形链表
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。



示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         dicNode = []
#         while head:
#             if head in dicNode:
#                 return True
#
#             dicNode.append(head)
#             head = head.next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        quick = head
        slow = head

        while quick and slow:
            slow = slow.next
            if quick.next:
                quick = quick.next.next
            else:
                return False

            if slow is quick:
                return True

        return False






