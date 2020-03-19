#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 2:15
# @Author  : yu.zhou
# @Email   : 524112470@qq.com
# @File    : p206.py
# @Software: PyCharm

"""
206. 反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        preNode = None
        while head:
            nextNode = head.next
            head.next = preNode
            preNode = head
            head = nextNode

        return preNode

