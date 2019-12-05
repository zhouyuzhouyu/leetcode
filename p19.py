# 19. 删除链表的倒数第N个节点

# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:


        if n <= 0:
            return head

        if not head:
            return head

        dic = {}
        count = 0
        dic[0] = head

        node = head
        while True:
            node = node.next
            if node:
                count += 1
                dic[count] = node

            else:
                break


        nodeDelete = dic.get(count-n+1)
        nodeBefor = dic.get(count-n)
        nodeNext = dic.get(count- n +2)


        if count - n + 1 < 0:
            return head
        elif count - n + 1 == 0:
            head.next = None
            return nodeNext
        else:
            nodeBefor.next = nodeNext
            nodeDelete.next = None
            return head






l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

print(Solution().removeNthFromEnd(l1,2))
