"""
139. 单词拆分
难度
中等

422

收藏

分享
切换为英文
关注
反馈
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tmpDic = {}
        def __wordBreak(s: str, wordDict: List[str], startIndex: int) -> bool:
            if len(s) == startIndex:
                return True

            if startIndex in tmpDic:
                return tmpDic[startIndex]

            for strW in wordDict:
                if s.startswith(strW, startIndex):
                    if __wordBreak(s, wordDict, startIndex+len(strW)):
                        tmpDic[startIndex] = True
                        return True

            tmpDic[startIndex] = False
            return False

        return __wordBreak(s, wordDict, 0)




s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

print(Solution().wordBreak(s, wordDict))
        