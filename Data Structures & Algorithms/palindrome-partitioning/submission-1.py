class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(i, curr):
            if i >= len(s):
                res.append(curr.copy())
                return

            for j in range(i, len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    curr.append(substring)
                    dfs(j+1, curr)
                    curr.pop()

        dfs(0, [])
        return res
        