import math 

class Solution:
    def jump(self, nums: List[int]) -> int:
        # @lru_cache(maxsize=None)
        # def traverse(n):
        #     if n >= (len(nums)-1):
        #         return 0
        #     minval = math.inf
        #     for i in range(1, nums[n]+1):
        #         minval = min(minval,  1 + traverse(n+i) )
        #     return minval
        # return traverse(0)
        dp = [0]*len(nums)
        dp[-1] = 0
        for i in range(len(nums)-2,-1,-1):
            # print(i)
            minval = math.inf
            for j in range(1, nums[i]+1):
                if j+i > (len(nums)-1):
                    val = 0
                else:
                    val = dp[j+i]
                minval = min(minval, 1 + val)
            dp[i] = minval

        return dp[0]
