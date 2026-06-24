# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        l, r = 1, length - 2

        while l <= r:
            m = (l + r) // 2
            left_val, mid_val, right_val = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)

            if left_val < mid_val < right_val:
                l = m + 1
            
            elif left_val > mid_val > right_val:
                r = m - 1

            else:
                break
        
        peak = m


        l, r = 0, peak

        while l <= r:
            m = (l + r) // 2
            mid_val = mountainArr.get(m)

            if mid_val < target:
                l = m + 1

            elif mid_val > target:
                r = m - 1

            else:
                return m
        
        l, r = peak, length - 1

        while l <= r:
            m = (l + r) // 2
            mid_val = mountainArr.get(m)

            if mid_val > target:
                l = m + 1
            
            elif mid_val < target:
                r = m - 1

            else:
                return m

        
        return -1

        