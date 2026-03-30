class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        target0exists = False
        target1exists = False
        target2exists = False

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            if not target0exists and t[0] == target[0]:
                target0exists = True

            if not target1exists and t[1] == target[1]:
                target1exists = True

            if not target2exists and t[2] == target[2]:
                target2exists = True

        return True if target0exists and target1exists and target2exists else False
        