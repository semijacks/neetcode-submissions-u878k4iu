class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substring = ''
                while stack[-1] != '[':
                    substring = stack.pop() + substring
                stack.pop()
                multiplier = ''
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
                stack.append(substring * int(multiplier))


        return ''.join(stack)
                

        