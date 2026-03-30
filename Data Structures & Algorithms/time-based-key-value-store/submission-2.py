class TimeMap:

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append((value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]


        print(f"time_map: {self.time_map}")
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.time_map:
            return res
        low = 0
        high = len(self.time_map[key]) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if self.time_map[key][mid][1] <= timestamp:
                res = self.time_map[key][mid][0]
                low = mid + 1
            else:
                high = mid - 1

        return res


        
