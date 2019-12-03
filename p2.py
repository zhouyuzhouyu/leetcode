# 两数相加
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        l1new = l1
        l2new = l2
        lresult = None
        lresultNew = None
        isBig = False
        while ((l1new is not None) or (l2new is not None)) or (isBig is True):
            lresultCurrent = None
            if lresultNew is None:
                lresult = ListNode(0)
                lresultNew = lresult
                lresultCurrent = lresultNew
            else:
                lresultCurrent = ListNode(0)
                lresultNew.next = lresultCurrent

            l1newVal = 0
            l2newVal = 0

            if l1new is not None:
                l1newVal = l1new.val

            if l2new is not None:
                l2newVal = l2new.val

            if isBig:
                lresultCurrent.val = l1newVal + l2newVal + 1
            else:
                lresultCurrent.val = l1newVal + l2newVal

            if lresultCurrent.val >= 10:
                isBig = True
                lresultCurrent.val -= 10
            else:
                isBig = False


            lresultNew = lresultCurrent
            if l1new is not None:
                l1new = l1new.next
            if l2new is not None:
                l2new = l2new.next

        return lresult



l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)

m1 = ListNode(5)
m2 = ListNode(6)
m3 = ListNode(4)

l1.next = l2
l2.next = l3
m1.next = m2
m2.next = m3

s = Solution().addTwoNumbers(l1,m1)

print(s.val)




