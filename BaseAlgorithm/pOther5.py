"""
有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""
"""
class Solution:
    dicCheck = {"()":0, "[]":0, "{}":0}

    def isValid(self, s: str) -> bool:
        if not s:
            return True
        elif len(s) == 1:
            return False
        elif len(s) == 2:
            if s in self.dicCheck:
                return True
            return False

        result = False
        for i in range(1, len(s)):
            if s[i-1:i+1] in self.dicCheck:
                ls = list(s)
                ls.pop(i-1)
                ls.pop(i-1)
                return self.isValid("".join(ls))


        return result

"""

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        dicCheck = {"(":")",")":"(","[":"]","]":"[","{":"}","}":"{",}
        listS = list(s)
        listCheck = []

        for i in range(len(listS)):
            if not listCheck:
                listCheck.append(listS[i])
                continue

            if dicCheck[listS[i]] == listCheck[-1]:
                listCheck.pop()
            else:
                listCheck.append(listS[i])


        return not listCheck



