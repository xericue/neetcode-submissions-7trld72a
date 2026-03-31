class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # given strings s and t
        # let's translate this into a hashmap
        # and then if the values of the hashmap s match the values
        # of the hashmap t then its a valid anagram
        # if "m" not in s_hm: return false

        s_hm = dict()
        t_hm = dict()

        for char in s:
            if char not in s_hm:
                s_hm[char] = 1
            else:
                s_hm[char] += 1

        for char in t:
            if char not in t_hm:
                t_hm[char] = 1
            else:
                t_hm[char] += 1
        
        # well the solution just says contain exact same characters
        # but that would entail numbers too so
        # whats a way we can compare all these numbers?
        if len(s_hm) != len(t_hm):
            return False
        else:
            # for key in s_hm[key]: <- WRONG IMPLEMENTATION
            for key in s_hm:
                # t_hm[r] doesnt exist so it literally wont run
                if key not in t_hm:
                    return False
                elif s_hm[key] != t_hm[key]:
                    return False

        return True