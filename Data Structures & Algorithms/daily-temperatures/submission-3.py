class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ret_arr = [0] * len(temperatures)
        stk = []

        # loop through the array
        for i in range(len(temperatures)):
            # monotonic stack solution
            # while the stack is not empty and the current temperature is greater than the
            # top of the stack, pop it so that you can use it for that respective index in
            # the return array
            while stk and temperatures[i] > temperatures[stk[-1]]:
                index = stk.pop() # the top element of the stack
                ret_arr[index] = i - index
                # why i - index?
                # oh because the problem is asking for the number of days before a warmer
                # temperature appears - so itll be the current index (the warmer temperature)
                # minus that previous index - so itll calculate the amount of days that have
                # passed

            # every iteration, we put something in the stack
            stk.append(i) # we put the current index so that we can index it later




        return ret_arr





























        """
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
        """