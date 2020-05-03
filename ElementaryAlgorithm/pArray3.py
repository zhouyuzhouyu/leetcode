"""
旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
"""

class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        k = k % len(nums)
        if k == 0:
            return

        tmp = nums[-1]
        for i in range(len(nums)):
            nums[i], tmp = tmp, nums[i]

        self.rotate(nums, k - 1)
        """

        k %= len(nums)

        def rev(nums: [int], start: int, end: int) -> None:
            nn = len(nums)
            n = (end - start) // 2 + 1
            for i in range(start, start + n):
                nums[i], nums[end - i + start] = nums[end-i + start], nums[i]

        rev(nums, 0, len(nums)-1)
        rev(nums, 0, k-1)
        rev(nums, k, len(nums)-1)





nums = [1,2,3,4]

Solution().rotate(nums, 2)

print(nums)