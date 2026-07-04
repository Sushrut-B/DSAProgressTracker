class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        if not nums:
            return 0
        cnt=0
        n=len(nums)
        max_cnt=0
        for i in range(n):
            if nums[i]==1:
                cnt+=1
                max_cnt=max(max_cnt,cnt)
            else:
                cnt=0
        return max_cnt