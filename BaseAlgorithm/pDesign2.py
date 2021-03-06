"""
最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。


示例:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.


提示：

pop、top 和 getMin 操作总是在 非空栈 上调用。
"""
from functools import reduce

import sys
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        self.minN = sys.maxsize


    def push(self, x: int) -> None:
        self.list.append(x)
        self.minN = min(self.minN, x)


    def pop(self) -> None:
        self.list.pop()


    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return reduce(min, self.list, sys.maxsize)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()