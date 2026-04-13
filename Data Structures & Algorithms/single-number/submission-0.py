class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_nums = nums[0]

        for i in range(1, len(nums)):
            xor_nums = xor_nums ^ nums[i]

        return xor_nums

        
        