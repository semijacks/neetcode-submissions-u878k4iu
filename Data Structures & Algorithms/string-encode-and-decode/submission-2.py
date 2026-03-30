class Solution:
    strLength = []

    def encode(self, strs: List[str]) -> str:
        self.strLength = []
        res = ""
        for index, value in enumerate(strs):
            if index == 0:
                self.strLength.append(len(value))
            else:
                self.strLength.append(self.strLength[index - 1]+len(value))
            res += value
        
        return res


    def decode(self, s: str) -> List[str]:
        res = []

        for index, value in enumerate(self.strLength):
            if index == 0:
                res.append(s[:value])
            else:
                res.append(s[self.strLength[index-1]:self.strLength[index]])

        return res
