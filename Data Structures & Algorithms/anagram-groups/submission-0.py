class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = strs
        return_arr = []

        for i in new_strs:
            temp = []
            new_new = sorted(i)
            # all new_news are now lexigraphically sorted lists of their letters
            # from here we can compare ???

            for j in range(len(new_strs)):
                new_new_2 = sorted(new_strs[j])
                if new_new == new_new_2:
                    temp.append(new_strs[j])
                    # break
            
            if temp in return_arr:
                continue
            else:
                return_arr.append(temp)

        # print(new_strs)

        return return_arr