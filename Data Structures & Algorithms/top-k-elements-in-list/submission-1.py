class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map={}
        for n in nums:
            freq_map[n]=freq_map.get(n, 0) + 1 

        #bucket
        bucket=[[]for _ in range(len(nums)+1)] 

        for num,freq in freq_map.items():
            bucket[freq].append(num)


        res=[]

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res