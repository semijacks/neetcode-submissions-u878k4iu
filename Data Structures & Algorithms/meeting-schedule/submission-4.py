"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        intervals.sort(key = lambda interval: interval.start)

        past_end = intervals[0].end
        
        for interval in intervals[1:]:
            if interval.start >= past_end:
                past_end = interval.end
                
            else:
                return False
        
        return True

