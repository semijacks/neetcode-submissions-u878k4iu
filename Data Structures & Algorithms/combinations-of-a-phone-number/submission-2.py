class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits == "": return res
        digit_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i, curr):
            if i == len(digits):
                res.append("".join(curr))
                return
            
            for c in digit_to_letter[digits[i]]:
                curr.append(c)
                dfs(i+1, curr)
                curr.pop()


        
        dfs(0, [])
        return res
        