class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = {}

        for i in range(len(nums)):
            
           
            goal = target - nums[i]

            if goal in hmap:
                return [hmap[goal],i]
            
            hmap[nums[i]] = i
        return []
            
        