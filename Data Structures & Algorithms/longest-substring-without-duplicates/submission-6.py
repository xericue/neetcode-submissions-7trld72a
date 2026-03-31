class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        
        # if not s:
        #     return max_len
        
        left, right = 0, 0

        while right < len(s):
            while s[right] in s[left:right]:
                left += 1

            max_len = max(max_len, len(s[left:right + 1]))

            right += 1

        return max_len