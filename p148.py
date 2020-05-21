"""
148. 排序链表
难度
中等

545

收藏

分享
切换为英文
关注
反馈
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        dicAll = {}
        while head:
            if head.val in dicAll:
                self.tmp += 0.0000001
                if head.val >= 0:
                    tmpVal = head.val + self.tmp
                else:
                    tmpVal = head.val - self.tmp
                dicAll[tmpVal] = head
            else:
                dicAll[head.val] = head
            nextHead = head.next
            head.next = None
            head = nextHead

        arrKey = list(dicAll.keys())
        arrKey.sort()

        if not arrKey:
            return None

        head = dicAll[arrKey[0]]
        preHead = head
        for i in range(1, len(arrKey)):
            preHead.next = dicAll[arrKey[i]]
            preHead = preHead.next

        return head


"""
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        mid, slow.next = slow.next, None

        left, right = self.sortList(head), self.sortList(mid)

        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next






l1 = ListNode(4)
l2 = ListNode(4)
l3 = ListNode(3)
l4 = ListNode(1)

l1.next = l2
l2.next = l3
l3.next = l4

print(Solution().sortList(l1))




