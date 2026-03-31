class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # how can i approach this with two pointers

        new = 0
        nnew = 1

        while nums and nnew < len(nums):
            if nums[new] == nums[nnew]:
                nums.pop(new)
                continue

            new += 1
            nnew += 1

        if len(nums) >= 2 and nums[-1] == nums[-2]:
                nums.pop(-1)

        return len(nums) 