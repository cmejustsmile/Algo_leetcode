class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        print(s)
        for c in s:
            if c == '[' or c =='{' or c == '(':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                cmp = stack.pop()
                if (cmp == '(' and c ==')') or (cmp == '[' and c == ']') or (cmp ==
                                                                             '{' and c == '}'):
                    continue
                else:
                    return False

        if len(stack) != 0:
            return False

        return True