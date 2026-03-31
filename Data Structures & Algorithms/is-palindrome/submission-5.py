class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1

        for i in s:
            # if its not alphanumeric, just skip it and
            # dont increment/move any pointer
            if s[left].isalnum() == False:
                left += 1
                continue
            
            if s[right].isalnum() == False:
                right -= 1
                continue

            # now we get into the logic
            # so if the left is NOT equal to the right:
            # return False

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            if left > right:
                break

        return True
