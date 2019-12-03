# 无重复字符的最长子串

# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        firstIndex = 0
        lastIndex = firstIndex + 1
        lenS = len(s)
        maxLength = 0
        dicAll = {}

        while (firstIndex < lenS+1) & (lastIndex < lenS+1):
            strS = s[firstIndex:lastIndex]
            # bSame = self.hasSame(s[firstIndex:lastIndex])
            bSame = s[lastIndex - 1] in dicAll
            if bSame:
                dicAll = {}
                index1 = s.index(s[lastIndex-1],firstIndex)
                index2 = lastIndex-1
                if index2-index1 - 1 > maxLength:
                    maxLength = index2 - index1 - 1

                firstIndex = index1+1
                lastIndex = firstIndex


            else:
                dicAll[s[lastIndex-1]] = 1
                if lastIndex-firstIndex > maxLength:
                    maxLength = lastIndex-firstIndex


            lastIndex += 1

        return maxLength




    def hasSame(self, s: str) -> bool:
        a = list(s)
        b = [x for x in range(len(a))]
        c = dict(zip(a,b))
        return len(c) != len(a)





# print(Solution().hasSame('abc'))
print(Solution().lengthOfLongestSubstring("abcabcdc"))
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len
'''