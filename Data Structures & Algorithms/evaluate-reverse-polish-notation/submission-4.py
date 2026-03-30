class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }
        

        for token in tokens:
            if token in ops:
                y = stack.pop()
                x = stack.pop()

                result = ops[token](x, y)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]


                
        