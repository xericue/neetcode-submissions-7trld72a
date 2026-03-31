class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # HASH MAP SOLUTION
        # two for loops, two hash maps, and a comparison: this is O(n)
        # wait because there are two distinct for loops, this is O(n + m).
        # must take multiple structures into account; its not all simplification
        countMap = {}
        compareMap = {}
        for char in s:
            if char not in countMap:
                countMap[char] = 1
            else:
                countMap[char] += 1
        
        for char_2 in t:
            if char_2 not in compareMap:
                compareMap[char_2] = 1
            else:
                compareMap[char_2] += 1

        if countMap == compareMap:
            return True
        else:
            return False
