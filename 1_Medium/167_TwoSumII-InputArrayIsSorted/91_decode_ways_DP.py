class Solution:
    def numDecodings(self, s):
        n = len(s)
        mem = [-1]*(n+2)
        def ways(i):
            if mem[i]!=-1:
                return mem[i]
            if i == n:
                mem[i] = 1
                return mem[i]
            if i > n:
                mem[i] = 0
                return mem[i]
            if s[i] == '0':
                mem[i] = 0
                return mem[i]
            ret = ways(i+1)
            if s[i] == '1':
                ret += ways(i+2)
            if s[i] == '2':
                if i+1 <= n-1:
                    if int(s[i+1]) <= 6:
                        ret += ways(i+2)
            mem[i] = ret
            return mem[i]

        return ways(0)
