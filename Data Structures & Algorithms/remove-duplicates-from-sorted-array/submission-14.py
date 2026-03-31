class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # how can i approach this with two pointers

        i = 0
        j = 1

        while nums and j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(i)
                continue # dont iterate i and j afterwards

            i += 1
            j += 1

        return len(nums) 