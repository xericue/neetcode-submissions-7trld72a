class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        # + or "C" or "D"
        # no need to worry about integers not existing, so we can just remove
        # as needed
        

        for op in operations:
            if op == "+":
                stk.append(stk[-1] + stk[-2])
            elif op == "C":
                stk.pop()
            elif op == "D":
                stk.append(stk[-1] * 2)
            else:
                # regularly append a score
                stk.append(int(op))
            
        # will need to aggregate a score
        ret_scr = 0
        for score in stk:
            ret_scr += score

        return ret_scr