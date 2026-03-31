class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ret_str = ''
        count = 0 
        while count != len(word1) and count != len(word2):
            ret_str += word1[count]
            ret_str += word2[count]
            count += 1

        if count < len(word1):
            ret_str += word1[count:]
        
        elif count < len(word2):
            ret_str += word2[count:]



        return ret_str