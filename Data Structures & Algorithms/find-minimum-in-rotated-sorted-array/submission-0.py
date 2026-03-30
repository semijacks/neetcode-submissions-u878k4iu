class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            # If middle is greater than rightmost, the minimum is in the right half
            if nums[mid] > nums[high]:
                low = mid + 1
            # Otherwise, the minimum is in the left half (including mid)
            else:
                high = mid
                
        return nums[low]
