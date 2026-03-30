class Solution:
    # Time Complexity - O(n) - iterating over length of array once
    # Space Completity - O(n) - using a set of length n in the worst case
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateSet = set()

        for i in range(len(nums)):
            if nums[i] in duplicateSet:
                return True
            else: 
                duplicateSet.add(nums[i])
        return False

         