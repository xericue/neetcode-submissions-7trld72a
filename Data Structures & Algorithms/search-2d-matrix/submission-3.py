class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            left = 0
            right = len(arr) - 1
            print(arr)
            while left <= right:
                mid = (left + right) // 2
                print(mid)
                if target == arr[mid]:
                    return True

                if target >= arr[mid]:
                    left = mid + 1

                else:
                    right = mid - 1
            


        
        return False