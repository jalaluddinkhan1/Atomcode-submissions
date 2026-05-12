class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if not nums or len(nums)<2:
            raise ValueError()
        
        seen: dict[int,int]={}  #value -> index

        for i,num in enumerate(nums):
            complement= target-num
            if complement in seen:
                return [seen[complement],i]
            seen[num]=i
        raise ValueError()
        