class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_num = {}
        seen = set()
        for i in nums:
            if i in seen:
                map_num[i] += 1
            else:
                map_num[i] = 1
                seen.add(i)
        sorted_num = sorted(map_num.items(), key=lambda item: item[1], reverse=True)
        sol = []
        for i in range(0,k):
            sol.append(sorted_num[i][0])
        return sol
