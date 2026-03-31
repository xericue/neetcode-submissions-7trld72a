class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # given an array, return true for any duplicate value
        # so we can try to brute force this and cycle through the
        # array, but that would take a while
        # we can map this all to a hash map to discern if there are
        # multiple values

        countMap = {}
        for i in nums:
            if i not in countMap:
                countMap[i] = 1
            else: 
                return True

        return False