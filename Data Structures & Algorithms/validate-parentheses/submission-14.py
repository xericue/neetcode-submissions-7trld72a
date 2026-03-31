class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = ['(', '{', '[']

        for i in s:
            if i in valid:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                elif i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False