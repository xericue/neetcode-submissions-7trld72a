class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stk = []

        for i in range(len(temperatures)):
            # check the top of the stack
            # check if the stack is empty
            while stk and temperatures[i] > temperatures[stk[-1]]:
                # if the value of temperatures at THAT index is smaller 
                # than our current value, pop it, take the popped value
                # (index), and go take the difference of indexes and 
                # put it into result[i].
                bruh = stk.pop()
                # ??? i think this is the index in the stack itself?
                result[bruh] = i - bruh


            # else, just append a regular index from a linear scan
            stk.append(i)
        return result