class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_dict = {}

        for i in range(len(nums)):
            nums_dict[nums[i]] = i

        for i in range(len(nums)):
            bruh = target - nums[i]
            if bruh in nums_dict:
                j = nums_dict[bruh]     
                if i != j:           
                    if i > j:  
                        return [j, i]
                    else:
                        return [i, j]

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             if i > j:
        #                 return [j, i]
        #             else:
        #                 return [i, j]