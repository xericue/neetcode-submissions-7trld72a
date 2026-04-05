class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        res = right

        while left <= right:
            weight_capacity = (left + right) // 2
            load = 0
            day = 1

            for weight in weights:
                if load + weight <= weight_capacity:
                    load += weight
                else:
                    day += 1
                    load = 0 + weight

            if day <= days:
                res = min(res, weight_capacity)
                right = weight_capacity - 1

            else:
                left = weight_capacity + 1

        return res
            