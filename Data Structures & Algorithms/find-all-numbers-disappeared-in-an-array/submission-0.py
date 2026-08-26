class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mark = [False] * n

        for num in nums:
            mark[num - 1] = True

        res = []
        for i in range(1, n + 1):
            if not mark[i - 1]:
                res.append(i)
        return res