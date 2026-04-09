class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
            
            tmp = curMin * n
            curMin = min(n * curMax, n * curMin, n)
            curMax = max(n * curMax, tmp, n)
            res = max(res, curMax)

        return res
        