"""
合并两个有序链表
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def __mergeTwoLists(l1: ListNode, l2: ListNode) -> None:
            if l1 and not l2:
                return l1
            elif l2 and not l1:
                return l2
            elif not l1 and not l2:
                return None

            if l1.val > l2.val:
                l1, l2 = l2, l1

            while l1:
                # if l1.val < l2.val and l1.next
                if l1.next:
                    if l1.next.val >= l2.val:
                        l1N = l1.next
                        l2N = l2.next
                        l1.next = l2
                        l2.next = l1N
                        __mergeTwoLists(l1, l2N)
                        break
                else:
                    l1.next = l2
                    break

                l1 = l1.next

        if l1 and not l2:
            return l1
        elif l2 and not l1:
            return l2
        elif not l1 and not l2:
            return None

        if l1.val > l2.val:
            l1,l2 = l2,l1
        __mergeTwoLists(l1,l2)

        return l1
