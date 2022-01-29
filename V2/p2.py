#!/usr/bin/python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1New = l1
        l2New = l2

        lNew = None
        lNewTemp = None

        s = 0

        while (l1New is not None) or (l2New is not None) or s != 0:
            l1V = 0
            l2V = 0

            if l1New is not None:
                l1V = l1New.val
                l1New = l1New.next

            if l2New is not None:
                l2V = l2New.val
                l2New = l2New.next

            r = l1V + l2V + s
            if r >= 10:
                r = r - 10
                s = 1
            else:
                s = 0

            if lNew is None:
                lNew = ListNode(r)
                lNewTemp = lNew
            else:
                lNewTemp.next = ListNode(r)
                lNewTemp = lNewTemp.next

            s = 4

        return lNew







