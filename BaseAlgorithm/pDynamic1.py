class Solution:
    dicA = {0:0,1:1,2:2}
    def climbStairs(self, n: int) -> int:
        # global dicA
        if n in self.dicA:
            return self.dicA[n]
        
        a = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.dicA[n] = a
        return a


print(Solution().climbStairs(5))