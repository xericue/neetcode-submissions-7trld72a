class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        right = len(nums) - 1
        left = 0

        while left <= right:
            if nums and nums[right] == val:
                nums.pop(right)
                right -= 1
            
            if nums and nums[left] == val:
                nums.pop(left)
                right -= 1

            else:
                left += 1


        return len(nums)