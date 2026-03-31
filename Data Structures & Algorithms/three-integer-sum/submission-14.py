class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret_arr = []

        f_map = {}
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            mid = i + 1
            right = len(nums) - 1
            
            
            while mid < right:
                if nums[i] + nums[mid] + nums[right] == 0 and (nums[i], nums[mid], nums[right]) not in f_map:
                    f_map[(nums[i], nums[mid], nums[right])] = 1
                    ret_arr.append([nums[i], nums[mid], nums[right]])
                
                # if nums[i] + nums[mid] + nums[right] == 0:
                #     if (nums[i], nums[mid], nums[right]) in f_map:
                #         continue
                #     else:
                #         f_map[(nums[i], nums[mid], nums[right])] = 1
                #         ret_arr.append([nums[i], nums[mid], nums[right]])
                
                elif nums[i] + nums[mid] + nums[right] > 0:
                    right -= 1
                
                else:
                    mid += 1
                
        return ret_arr


























        # ret_arr = []
        # snums = sorted(nums)

        # f_map = {}

        # # fix one element to lessen the complexity of the problem
        # for i in range(len(snums)):
        #     left = i + 1
        #     right = len(nums) - 1
            
        #     # use our regular two pointers method otherwise
        #     # this works well because our array is sorted!
        #     while left < right:
        #         if snums[i] + snums[left] + snums[right] == 0 and (snums[i], snums[left], snums[right]) not in f_map:
        #             ret_arr.append([snums[i], snums[left], snums[right]])
        #             f_map[(snums[i], snums[left], snums[right])] = 1
        #         elif snums[i] + snums[left] + snums[right] > 0:
        #             right -= 1
        #         else:
        #             left += 1
        # return ret_arr