class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # return the indexes
        # cannot use the same index twice

        # since its increasing/already sorted
        # if the given answer is greater than target:
            # move right down
        # if the given answer is less than target:
            # move left up

        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            
            elif numbers[left] + numbers[right] > target:
                right -= 1
            
            elif numbers[left] + numbers[right] < target:
                left += 1