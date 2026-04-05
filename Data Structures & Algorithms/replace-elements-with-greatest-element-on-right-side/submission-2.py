class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        ret_arr = [0] * len(arr)
        new_max = -1


        for i in range(len(arr) - 1, -1, -1):
            ret_arr[i] = new_max
            new_max = max(arr[i], new_max)

        return ret_arr