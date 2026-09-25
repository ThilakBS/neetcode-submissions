class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,a in enumerate(nums):
            gap = target-a
            if gap in seen:
                return [seen[gap],i]
            else:
                seen[a] = i
        print(seen)
        return []