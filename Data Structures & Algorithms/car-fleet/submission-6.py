class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # define each car in an array of tuples
        arr = []

        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        
        arr.sort(reverse=True)

        stk = []

        for j in arr:
            stk.append((target - j[0]) / j[1])
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()

        return len(stk)