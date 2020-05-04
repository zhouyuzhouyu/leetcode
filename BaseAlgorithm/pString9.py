"""
最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""

class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if not strs:
            return ""

        str0 = strs[0]
        if not str0:
            return ""

        listCommon = []
        # def __longestCommonPrefix(strA: str, index: int):
        for i in range(len(str0)):
            str0i = str0[i]
            result = True
            for j in range(len(strs)):
                try:
                    if str0i != strs[j][i]:
                        result = False
                        break
                except Exception as e:
                    result = False
                    break

            if result:
                listCommon.append(str0i)
            else:
                break

        return "".join(listCommon)


print(Solution().longestCommonPrefix(["flower","flow","flight"]))