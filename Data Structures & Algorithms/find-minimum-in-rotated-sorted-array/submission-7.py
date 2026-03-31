class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # if nums[mid] == min(nums):
            #     return nums[mid]

            if nums[mid] < nums[right]: # left half is sorted
                    right = mid
            else:
                left = mid + 1

        return nums[left]