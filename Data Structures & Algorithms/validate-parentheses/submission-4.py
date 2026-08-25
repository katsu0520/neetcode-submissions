class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif not stack:
                return False
            else:
                if stack[-1] == "(" and c == ")":
                    stack.pop()
                elif stack[-1] == "{" and c == "}":
                    stack.pop()
                elif stack[-1] == "[" and c == "]":
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
