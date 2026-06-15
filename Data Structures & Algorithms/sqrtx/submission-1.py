class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x

        while L <= R:

            mid = (L + R) // 2
            sqrt = mid * mid 

            if sqrt < x:
                L = mid + 1
            elif sqrt > x:
                R = mid - 1
            else:
                return mid
            
        return R
