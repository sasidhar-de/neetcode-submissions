class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {} 
        for idx, val in enumerate(nums): 
            if target - val in seen_dict: 
                return [seen_dict[target - val], idx] 

            seen_dict[val] = idx