#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 2:39
# @Author  : yu.zhou
# @Email   : 524112470@qq.com
# @File    : p234.py
# @Software: PyCharm

"""
234. 回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        listA = []
        while head:
            listA.append(head.val)
            head = head.next

        return listA == listA[::-1]

