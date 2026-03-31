class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                # what we just found is greater, so go down
                right = mid - 1

            else:
                left = mid + 1

        # so mid is one off from the index from where its supposed to be
        # i think this is gonna depend on the indexing...


        if nums[mid] < target:
            return mid + 1
        else:
            return mid




