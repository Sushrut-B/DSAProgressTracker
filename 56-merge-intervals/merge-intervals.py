class Solution(object):
    def merge(self, intervals):
        # Your code goes here
        if not intervals:
            return []
        intervals.sort()
        ans=[]
        ans.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1]=max(ans[-1][1],intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans