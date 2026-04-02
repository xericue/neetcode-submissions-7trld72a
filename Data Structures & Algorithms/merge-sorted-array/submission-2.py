class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # So it's easier to go from the back???????? I think it's because
        # the space is already there and we don't have to shift every element
        # down - we can just move things one by one.

        end = len(nums1) - 1
        while end >= 0:
            if m - 1 >= 0 and n - 1 >= 0:
                if nums1[m - 1] > nums2[n - 1]:
                    nums1[end] = nums1[m - 1]
                    end -= 1
                    m -= 1
                else:
                    nums1[end] = nums2[n - 1]
                    end -= 1
                    n -= 1

            elif n - 1 >= 0:
                nums1[end] = nums2[n - 1]
                end -= 1
                n -= 1
            
            else:
                # deeuurrrr because thats the ending condition. we need end -= 1
                # to decrement regardless since thats the condition the while
                # loop depends on. 
                return