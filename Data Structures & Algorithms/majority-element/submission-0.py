class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # just looks like a frequency map

        f_map = {}

        for i in nums:
            f_map[i] = f_map.get(i, 0) + 1

        # 5: 4
        # 1: 3
        max_val = 0

        for i, val in f_map.items():
            if val == max(f_map.values()):
                max_val = i

        return max_val