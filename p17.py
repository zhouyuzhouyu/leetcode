# 17. 电话号码的字母组合

# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        dicAll = {}
        count = 0
        index = 2
        for i in range(97,123):
            b = dicAll.get(str(index))

            if not b:
                b = []
                dicAll[str(index)] = b
            b.append(chr(i))

            count += 1
            if (index == 7) | (index == 9):
                if count >= 4:
                    count = 0
                    index += 1
            else:
                if count >= 3:
                    count = 0
                    index += 1

        resR = []
        for index,s in enumerate(digits):
            if index == 0:
                resR = dicAll[s]
                continue
            resR = [m + n for m in resR for n in dicAll[s]]
        return resR


print(Solution().letterCombinations('23'))

