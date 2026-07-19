class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        prev=self.countAndSay(n-1)
        cnt,i=1,1
        res=""

        for i in range(1, len(prev)):
            if prev[i] == prev[i-1]:
                cnt+=1
            else:
                res += str(cnt)
                res+=prev[i-1]
                cnt = 1
        res += str(cnt)
        res += prev[-1]
        return res



   