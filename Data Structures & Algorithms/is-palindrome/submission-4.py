class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1
        count = 0

        for i in s:
            print(f"iteration {count}")
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
            print(f"left = {s[left].lower()}, right = {s[right].lower()}")
            print(f"left is {left}, right is {right}")

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            count += 1
            if left > right:
                break

        return True
