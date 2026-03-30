class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = dict()

        for char_s in s: 
            if char_s in map:
                map[char_s] = map[char_s] + 1
            else:
                map[char_s] = 1
        
        for char_t in t:
            if not char_t in map:
                return False
            
            if map[char_t] == 1:
                del map[char_t]
            else:
                map[char_t] = map[char_t] - 1
        
        if not map:
            return True
        else: 
            return False
        