class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_jump_end = 0
        farthest_reach = 0

        for i in range(len(nums) - 1):
            farthest_reach = max(farthest_reach, nums[i] + i)

            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest_reach

            if i == len(nums) - 1:
                break

        return jumps


        