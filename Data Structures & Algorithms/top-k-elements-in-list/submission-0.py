class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {} 
        for i in nums : 
            count_dict[i] = 1 + count_dict.get(i,0) 

        arr = [] 
        for key, val in count_dict.items() : 
            arr.append([val, key])

        arr.sort(reverse=True)
        res = [] 

        for idx in range(k) : 
            res.append(arr[idx][1])

        return res 