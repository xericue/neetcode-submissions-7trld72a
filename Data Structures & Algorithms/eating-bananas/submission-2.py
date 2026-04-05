class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)

        result = right

        while left <= right:
            mid = (left + right) // 2 # this is a test answer from our answer space

            # now how do we apply it to this problem in specific?
            total_bananas_eaten = 0

            for bananas in piles:
                total_bananas_eaten += math.ceil(bananas / mid) # bananas / bananas per hour 

            if total_bananas_eaten <= h:
                result = min(result, mid)
                right = mid - 1

            else:
                left = mid + 1


        return result