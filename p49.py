"""
49. 字母异位词分组
难度
中等

335

收藏

分享
切换为英文
关注
反馈
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        class __strData:
            def __init__(self, str1: str):
                self.str1 = str1
                self.sortStr = sorted(str1)

        result: List[List[__strData]] = []
        # strs.sort()

        strsData = map(__strData, strs)

        def __groupAnagram(strData: __strData) -> None:
            if not result:
                result.append([strData])
                return

            isIn = False
            for strsData in result:
                if strsData[0].sortStr == strData.sortStr:
                    strsData.append(strData)
                    isIn = True
                    break

            if not isIn:
                result.append([strData])

        for strData in strsData:
            __groupAnagram(strData)

        return list(map(lambda x:list(map(lambda y:y.str1,x)) ,result))


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))