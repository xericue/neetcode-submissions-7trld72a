class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
                print(left)
                print(s[left])
            while left < right and not s[right].isalnum():
                right -= 1

            print(left)
            print(s[left])
            if s[left].lower() != s[right].lower():
                return False
            
            else:
                right -= 1
                left += 1
        

        return True