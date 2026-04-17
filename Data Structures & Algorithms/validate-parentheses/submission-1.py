class Solution:
    def isValid(self, s: str) -> bool:
        closed_to_open = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i in closed_to_open:
                if stack and stack[-1] == closed_to_open[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        return True