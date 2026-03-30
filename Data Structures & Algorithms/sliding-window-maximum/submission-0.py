class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        l = 0

        for r in range(k - 1, len(nums)):
            prevL = l
            max_window = nums[l]

            while l <= r:
                max_window = max(max_window, nums[l])
                l += 1
            
            output.append(max_window)
            l = prevL
            l += 1

        return output
                
        