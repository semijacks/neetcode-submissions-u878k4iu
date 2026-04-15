class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(0, n+1):
            count = 0
            while i > 0:
                bit = i & 1
                count = count + 1 if bit == 1 else count
                i >>= 1
            ans.append(count)
        
        return ans

        