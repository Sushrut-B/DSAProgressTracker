class Solution(object):
    def majorityElement(self, nums):
        count=0
        element=0
        for i in range(len(nums)):
            if count==0:
                element=nums[i]
                count=1
            elif nums[i]==element:
                count+=1
            else:
                count-=1
        cnt1=0
        for i in range(len(nums)):
            if nums[i]==element:
                cnt1+=1
        if cnt1>(len(nums))//2:
            return element
        else:
            return 0
            