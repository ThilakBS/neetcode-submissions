class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2*n
        for i,t in enumerate(nums):
            ans[i] = t
            ans[n+i] = t
        return ans
