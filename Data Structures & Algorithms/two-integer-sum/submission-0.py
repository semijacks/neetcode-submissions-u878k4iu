class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_set = set()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diff_set:
                return [nums.index(diff), i]
            else:
                diff_set.add(nums[i])

        
