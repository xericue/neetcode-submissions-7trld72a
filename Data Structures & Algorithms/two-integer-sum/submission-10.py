class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f_map = {}

        # make a dictionary where you can get the index from a value

        for i, value in enumerate(nums):
            j = target - value
            if j in f_map:
                if f_map[j] > i:
                    return [i, f_map[j]]
                else:
                    return [f_map[j], i]
            # if its not there yet, add it
            f_map[value] = i