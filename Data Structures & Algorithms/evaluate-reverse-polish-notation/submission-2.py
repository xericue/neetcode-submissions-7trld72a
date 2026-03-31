class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # list of strings 
        
        stk = []

        for i in tokens:
            if i == '+':
                temp = stk.pop()
                temp_2 = stk.pop()
                stk.append(temp + temp_2)
            elif i == '-':
                temp = stk.pop()
                new = stk.pop()
                new = new - temp
                stk.append(new)
            elif i == '*':
                temp = stk.pop()
                temp_2 = stk.pop()
                stk.append(temp * temp_2)
            elif i == '/':
                temp = stk.pop()
                new = stk.pop()
                stk.append(int(new / temp))
            else:
                stk.append(int(i))

            print(stk)

        return stk[0]