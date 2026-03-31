class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # problem is already in ascending order
        # find the index of a specific target in the integer

        # half the search array every single time until we can lowkenuinely find the solution

        # which can be done iteratively and recursively but i think its better done iteratively

        left = 0
        right = len(nums) - 1

        while left <= right:
	        mid = (right + left) // 2 # floors
	        if nums[mid] == target:
		        return mid
		
	        elif nums[mid] < target:
    		    left = mid + 1
	
	        else:
		        right = mid - 1

        return -1
        
        
