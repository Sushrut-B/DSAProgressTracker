class Solution(object):
    def maxSubArray(self, nums):
        maxi=nums[0]
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
            if sum1 > maxi :
                maxi=sum1
            if sum1<0:
                sum1=0
        return maxi