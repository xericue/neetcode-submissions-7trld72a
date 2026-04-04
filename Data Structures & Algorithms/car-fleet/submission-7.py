class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # define each car in an array of tuples so that we can sort the whole array 
        # according to its position according to which car is closest first. this 
        # allows us to process each car whose closest to the target, meaning we get 
        # to process if the cars further from the target will merge with the ones 
        # ahead of it (which works much easier by the nature of the sorted array).

        new_arr = [(pos, sp) for pos, sp in zip(position, speed)]

        stk = []
        # optimal solution will use a monotonic stack to pop a car every time it 
        # merges, leaving us with the amount of fleets (amount of times where the 
        # closest car arrives uninterrupted) BECAUSE the closest car will always 
        # have the greatest time, and so each car fleet from then will have a 
        # STRICTLY LESSER time, making our stack monotonically decreasing
        for pos, sp in sorted(new_arr)[::-1]:
            stk.append((target - pos) / sp)

            # if we can actually consider a merge (if there are two or more cars) 
            # and if the newest car added (a car with a further position) has a 
            # lesser time than the car closer to the target
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()

        return len(stk)