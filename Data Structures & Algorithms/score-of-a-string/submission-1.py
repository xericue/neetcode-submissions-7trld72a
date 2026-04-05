class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        for char_idx in range(1, len(s)):
            score += abs(ord(s[char_idx]) - ord(s[char_idx - 1]))

        return score
