class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # so i think you not only want the two elements with the least difference
        # but also the indices with the greatest distance

        # so we're definitely going to be keeping a min diff and max el_diff
        # with an initial pass here

        # this may benefit most from using two pointers just because we want to enclose
        # the maximum number of elements, meaning we start from the left and the right
        # and greedily decrease right/increase left

        left = 0
        right = len(heights) - 1

        best = 0
        
        while left < right:
            best = max(best, (min(heights[left], heights[right]) * abs(left - right)))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        # the answer is going to be the smallest height (of the two pointers) 
        # multiplied by the length between the two indexes so this is truly a greedy
        # problem that needs to have maxes

        return best