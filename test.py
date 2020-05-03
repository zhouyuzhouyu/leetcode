a = [1,2,3]
b = [1,2,3]

print(a == b)

print(sorted(a,reverse=True))


class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        dicA = {}
        for i in range(len(nums)):
            dicA[nums[i]] = 0

        numsD = list(dicA.keys())
        for i in range(len(numsD)):
            nums[i] = numsD[i]

        return len(numsD)



print(Solution().removeDuplicates([1,1,1,2]))


score_you = 0
def kickedBall(shooter, goalkeeper):
    global score_you
    score_you = max(score_you, 3)
kickedBall("myNanme", "com")

print(score_you)