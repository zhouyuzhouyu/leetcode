"""
31. 下一个排列
难度
中等

实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # maxNums = sorted(nums, reverse=True)
        # if maxNums == nums:
        #
        #     return sorted(nums)

        def sortNum(numsAll: [int], start: int):
            ll = len(numsAll)
            for ii in range(start, ll):
                for jj in range(ii+1, ll):
                    if nums[ii] > nums[jj]:
                        nums[ii], nums[jj] = nums[jj], nums[ii]



        le = len(nums)
        for i in reversed(range(1, le)):
                if nums[i] > nums[i-1]:
                    # nums[i], nums[i-1] = nums[j], nums[i]
                    # sortNum(nums, j+1)
                    for j in reversed(range(i, le)):
                        if nums[j] > nums[i-1]:
                            nums[i-1], nums[j] = nums[j], nums[i-1]
                            sortNum(nums,i)
                            return

        nums.sort()




print(Solution().nextPermutation([1,3,2]))