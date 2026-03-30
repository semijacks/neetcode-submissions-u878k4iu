class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        char_count_s1, char_count_s2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            char_count_s1[ord(s1[i]) - ord('a')] += 1
            char_count_s2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += 1 if char_count_s1[i] == char_count_s2[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            char_count_s2[index] += 1
            if char_count_s1[index] == char_count_s2[index]:
                matches +=1
            elif char_count_s1[index] + 1 == char_count_s2[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            char_count_s2[index] -= 1
            if char_count_s1[index] == char_count_s2[index]:
                matches += 1
            elif char_count_s1[index] - 1 == char_count_s2[index]:
                matches -= 1
            
            l += 1

        return matches == 26
        