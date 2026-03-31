class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # implement binary search
        # split the array in half every time based on if nums[x] >/< target

        # use two pointers for the subsection

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # if the current number is smaller: its in the upper half
            elif nums[mid] < target:
                left = mid + 1
            # if the current number is larger: its in the lower half so put down right
            else:
                right = mid - 1
            

        return -1
        
