class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {} #key: letter, value: occurance
        t_dict = {}

        for lttr in s:
            s_dict[lttr] = s_dict.get(lttr, 0) + 1

        for lttr in t:
            t_dict[lttr] = t_dict.get(lttr, 0) + 1

        for lttr in s_dict.keys():
            if lttr not in t_dict.keys():
                return False
            if s_dict[lttr] != t_dict[lttr]:
                return False
        
        return True