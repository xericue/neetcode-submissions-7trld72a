class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # so i gotta Sort ts? gang cant i just Sort ts Gang cant I just Sort ts

        bruh = sorted(set(nums))

        if len(nums) == 0:
            return 0

        print(bruh)
        count = best = 1   

        for i in range(1, len(bruh)):
            if bruh[i - 1] == bruh[i] - 1:
                count += 1
                if count > best:
                    best = count

            else:
                count = 1

        return best