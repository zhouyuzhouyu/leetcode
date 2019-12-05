# 21. 合并两个有序链表

# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l: ListNode

        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            l = l1
            p1 = l1
            p2 = l2
        else:
            l = l2
            p1 = l2
            p2 = l1
            l1 = p1
            l2 = p2

        while p2:
            pTemp: ListNode = p1
            pTemp2: ListNode = p2
            if p1.val <= p2.val:
                if p1.next:
                    if p1.next.val >= p2.val:
                        pTemp2 = p2.next
                        pTemp = p1.next
                        p1.next = p2
                        p2.next = pTemp
                    else:
                        p1 = p1.next
                else:
                    pTemp2 = p2.next
                    p1.next = p2
                    p2.next = None

            else:
                print('error')
                break



            p2 = pTemp2


        return l


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(4)

l4 = ListNode(1)
l5 = ListNode(3)
l6 = ListNode(4)

l1.next = l2
l2.next = l3
l4.next = l5
l5.next = l6

print(Solution().mergeTwoLists(l1,l4))
