class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        ret_arr = arr

        for i in range(len(arr) - 1):
            ret_arr[i] = max(ret_arr[i + 1:])

        ret_arr[-1] = -1

        return ret_arr