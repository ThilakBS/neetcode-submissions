class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for i in range(len(nums)):
            difference = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == difference:
                    return [i,j]