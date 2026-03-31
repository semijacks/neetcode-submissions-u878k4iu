class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []

        for i, char in enumerate(s):
            if char == "(":
                left_stack.append(i)
            elif char == "*":
                star_stack.append(i)
            else:
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        while left_stack and star_stack:
            left, star = left_stack.pop(), star_stack.pop()
            if left > star:
                return False

        return not left_stack
        