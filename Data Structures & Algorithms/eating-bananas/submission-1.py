class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # we're actually doing a binary search on our rates
        left = 1
        right = max(piles)
        result = right

        # this is giving us a new rate every single time
        while left <= right:
            # which is why we re-calculate total hours
            new_rate = (left + right) // 2
            total_hours = 0


            for pile in piles:
                total_hours += math.ceil(pile / new_rate)
            
            print(total_hours)
            if total_hours <= h:
                result = min(result, new_rate)
                right = new_rate - 1
                
            else:
                left = new_rate + 1

        return result