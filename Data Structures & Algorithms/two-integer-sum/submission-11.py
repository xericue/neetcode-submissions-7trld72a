class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f_map = {}

        # make a dictionary where you can get the index from a value

        for i, value in enumerate(nums):
            # calculate the complement and check if it exists in the f_map 
            # (which is our list of values in the entire array itself!)
            j = target - value

            # if it's there, return it
            if j in f_map:
                if f_map[j] > i:
                    return [i, f_map[j]]
                else:
                    return [f_map[j], i]

            # if its not there yet, add it (doing it else with the f_map prevents dups)
            f_map[value] = i