# 22. 括号生成

# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/generate-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        result = set()

        def generate(l:[]):
            result = set()
            for s in l:
                for index1 in range(len(s)+1):
                    s1 = s[:]
                    listS1 = list(s1)
                    listS1.insert(index1, '(')
                    s1 = ''.join(listS1)
                    for index2 in range(1,len(s1)+1):
                        listS1 = list(s1)
                        listS1.insert(index2, ')')
                        s2 = ''.join(listS1)
                        if self.isValid(s2):
                            result.add(s2)
            return  result

        for _ in range(n):
            if not result:
                result.add("()")
                continue
            result = generate(result)

        return list(result)

    def isValid(self, s: str) -> bool:
        while True:
            a = s.replace("()", "")
            ba = (a != s)
            s = a

            if not ba:
                break
        return not bool(s)


print(Solution().generateParenthesis(6))