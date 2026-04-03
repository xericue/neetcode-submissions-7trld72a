class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        middle_array = []

        while left <= right:
            # middle_element = (left_arr[0] + right_arr[0]) // 2
            mid = (left + right) // 2
            if target == matrix[mid][0] or target == matrix[mid][len(matrix[mid]) - 1]:
                return True
            
            if target > matrix[mid][0] and target < matrix[mid][len(matrix[mid]) - 1]:
                middle_array = matrix[mid]
                break

            elif target > matrix[mid][0]:
                left = mid + 1
            
            else:
                right = mid - 1


        
        left = 0
        right = len(middle_array) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if target == middle_array[mid]:
                return True

            if target >= middle_array[mid]:
                left = mid + 1

            else:
                right = mid - 1
        return False