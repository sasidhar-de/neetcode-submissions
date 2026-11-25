class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # handle edge case 
        if len(s) != len(t) : 
            return False 

        s_count, t_count = {}, {} 

        for idx in range(len(s)) : 
            s_count[s[idx]] = 1 + s_count.get(s[idx], 0)
            t_count[t[idx]] = 1 + t_count.get(t[idx], 0)

        return s_count == t_count 