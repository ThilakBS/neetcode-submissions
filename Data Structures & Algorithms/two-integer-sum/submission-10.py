class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,a in enumerate(nums):
            seen[i] = a
            if i>0:
                for j in range(i):
                    if a+seen[j] == target:
                        return [j,i]

            



