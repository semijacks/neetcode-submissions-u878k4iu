class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_map = {char: i for i, char in enumerate(s)}
        res = []
        curr_size = 0
        curr_end = 0

        for i, char in enumerate(s):
            curr_size += 1
            curr_end = max(curr_end, last_map[char])

            if i == curr_end:
                res.append(curr_size)
                curr_size = 0
        return res



        

        