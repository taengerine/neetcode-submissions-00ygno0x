class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1 
        curr = 1

        for i in range(n):
            temp = curr
            curr = curr + prev 
            prev = temp

        return temp
        