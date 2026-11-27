class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)

        freq_count = [[] for _ in range(len(nums) + 1)]
        for key, val in count_dict.items():
            freq_count[val].append(key)

        res = []
        for idx in range(len(freq_count) - 1, 0, -1):
            for num in freq_count[idx]:
                res.append(num)
                if len(res) == k:
                    return res