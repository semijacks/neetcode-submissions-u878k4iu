class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        target = len(nums)//3
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

            if count[num] > target:
                if not num in res:
                    res.append(num)

        return res

        