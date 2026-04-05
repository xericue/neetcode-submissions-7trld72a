class Solution:
    def mySqrt(self, x: int) -> int:
        # return the square root of x rounded down
        if x == 0:
            return 0
        elif x == 1:
            return 1

        # search the space from 1 to x // 2

        left = 1
        right = x // 2
        res = 0

        while left <= right:
            mid = (right + left) // 2

            if x // mid == mid:
                return mid
            
            elif x // mid > mid:
                left = mid + 1
                res = mid
            
            else:
                right = mid - 1

        return res