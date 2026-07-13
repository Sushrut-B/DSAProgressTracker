class Solution(object):
    def topKFrequent(self, nums, k):
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        sorted_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(sorted_freq[i][0])
        return ans
