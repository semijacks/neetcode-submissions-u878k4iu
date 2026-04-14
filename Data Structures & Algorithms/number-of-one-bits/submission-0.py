class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n > 0:
            bit = n & 1
            res = res + 1 if bit == 1 else res
            n >>= 1
        
        return res
        