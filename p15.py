# 15. 三数之和

# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution:
    def threeSum(self, nums:[int]) -> [[int]]:
        r = {}
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                s = nums[i] + nums[j]
                for k in range(n):
                    if (k != i) & (k != j) & (s+nums[k] == 0):
                        sortL = sorted([nums[i],nums[j],nums[k]])
                        r[str(sortL[0])+str(sortL[1])] = sortL

        return list(r.values())
'''

class Solution:
    def threeSum(self, nums:[int]) -> [[int]]:
        sortNums = sorted(nums)
        n = len(sortNums)
        i = 0
        res = {}
        if n < 3:
            return []

        for i in range(n):

            l = i + 1
            r = n - 1
            while l < r:
                s = sortNums[i] + sortNums[l] + sortNums[r]
                if s == 0:
                    res[str(sortNums[i])+str(sortNums[l])] = [sortNums[i] , sortNums[l] , sortNums[r]]
                    l += 1
                    r -= 1
                elif s >= 0:
                    r -= 1
                else:
                    l += 1

            if sortNums[i] >= 0:
                break

        return list(res.values())








print(Solution().threeSum([0,0,0,0]))

