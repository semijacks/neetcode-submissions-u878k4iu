class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCnt = 0
        cnt = 0

        for num in nums:

            if num == 1:
                cnt += 1
            else:
                maxCnt = max(maxCnt, cnt)
                cnt = 0

        maxCnt = max(maxCnt, cnt)

        return maxCnt
        