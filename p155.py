#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 5:59
# @Author  : yu.zhou
# @Email   : 524112470@qq.com
# @File    : p155.py
# @Software: PyCharm

"""
155. 最小栈
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

class MinStack:

    def __init__(self):
        # initialize your data structure here.



    def push(self, x: int) -> None:


    def pop(self) -> None:


    def top(self) -> int:


    def getMin(self) -> int:



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.myList = []

    def push(self, x: int):
        self.myList.append(x)

    def pop(self):
        self.myList.pop()

    def top(self) -> int:
        if not self.myList:
            return None
        return self.myList[-1]

    def getMin(self) -> int:
        if not self.myList:
            return None
        return min(self.myList)



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()