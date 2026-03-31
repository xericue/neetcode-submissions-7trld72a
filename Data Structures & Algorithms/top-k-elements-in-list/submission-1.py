class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fmap = {}
        return_array = []
        temp_k = k # so we can decrement it

        for i in nums:
            if i not in fmap:
                fmap[i] = 1
            else:
                fmap[i] += 1

        # now we have the key of the number linked to respective frequencies

        for i in range(k):
            highest = 0
            index = 0
            for j in fmap:
                if fmap[j] > highest:
                    highest = fmap[j]
                    index = j
            
            fmap[index] = 0
            return_array.append(index)

        return return_array



