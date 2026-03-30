class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0


        for num in nums_set:
            if (num - 1) not in nums_set:
                curr_count = 0
                while num + curr_count in nums_set:
                    curr_count += 1
            
                max_count= max(max_count, curr_count)

        return max_count



        