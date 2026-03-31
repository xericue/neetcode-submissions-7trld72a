class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        # so at the end, the number will be zero to one numbers off

        # i.e. if we had -2, we would wanna give 0. mid would be 0
        # and put it in 0
        # if we had 5, we're looking at 4 (index 3)
        # so mid is equal to 3 but we wanna put it in 4
        # i.e. if nums[mid] = 4 and we have 5
        # if nums[mid] < target:

        print(mid)
        print(nums[mid])
        if nums[mid] < target:
            return mid + 1
        elif nums[mid] > target:
            if mid - 1 < 0:
                return mid
            else:
                return mid
        else:
            return mid