"""
整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""
import sys


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -1 * x
        elif x == 0:
            return 0

        lx = list(str(x))
        lx.reverse()
        i = 0
        while i < len(lx):
            if lx[i] == "0":
                lx.pop(i)
            else:
                break

        strResult = "".join(lx)
        result = int(strResult) * sign
        if result > (pow(2,31) - 1) or result < pow(-2,31):
            return 0

        return result

print(Solution().reverse(0))