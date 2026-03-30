class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                last_temp, last_temp_idx = stack.pop()
                output[last_temp_idx] = i - last_temp_idx
            
            stack.append([t, i])

        return output
        