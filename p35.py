"""
39. 组合总和
难度
中等

626

收藏

分享
切换为英文
关注
反馈
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

class Solution:

    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        result = []
        if not candidates:
            return result

        def findCom(candidates: [int], target: int, ll: [int]):
            if target == 0:
                result.append(ll)
                return

            if target > 0:
                for i in range(len(candidates)):
                    if ll and ll[-1] < candidates[i]:
                        continue
                    ll.append(candidates[i])
                    findCom(candidates, target-candidates[i], ll)
                    ll.pop(-1)

        findCom(candidates, target,[])

        return result



print(Solution().combinationSum([2,3,6,7],7))


