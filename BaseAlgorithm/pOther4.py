"""
帕斯卡三角形
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution:
    def generate(self, numRows: int) -> [[int]]:
        if numRows < 1:
            return None
        if numRows == 1:
            return [[1]]

        listPre = self.generate(numRows-1)
        listP = listPre[-1]
        listC = [1]
        for i in range(1,len(listP)):
            listC.append(listP[i-1]+listP[i])
        listC.append(1)

        listPre.append(listC)

        return listPre


print(Solution().generate(5))



