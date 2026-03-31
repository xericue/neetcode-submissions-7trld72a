class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix sum
        n = len(nums)
        output = [1] * n
        pref = 1 # BECAUSE THERES NO PREFIX TO THE FIRST ELEMENT... SO ITS
        # JUST THE FIRST ELEMENT MULTIPLIED BY ITSELF !!!

        # the end goal is multiplying all numbers by all other numbers
        # except by themselves

        # first pass: multiply an array element by everything before it
        for i in range(1, n):
            pref *= nums[i - 1]
            output[i] = pref

        npref = 1
        # ermmm why you gotta set it to 1 first twin

        # second pass: multiply an array element by everything after it
        for j in range(n - 2, -1, -1):
            npref *= nums[j + 1]
            output[j] *= npref
        return output