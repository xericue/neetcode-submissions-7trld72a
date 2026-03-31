class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f_map = {}

        # make a dictionary where you can get the index from a value

        for x, value in enumerate(nums):
            j = target - value
            if j in f_map:
                if f_map[j] > x:
                    return [x, f_map[j]]
                else:
                    return [f_map[j], x]
            f_map[value] = x