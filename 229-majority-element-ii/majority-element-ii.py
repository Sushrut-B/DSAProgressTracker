class Solution(object):
    def majorityElement(self, nums):
        cnt1=0
        cnt2=0
        ele1=0
        ele2=0
        n=len(nums)
        for i in range(n):
            if nums[i] == ele1 and nums[i]!= ele2:
                cnt1 += 1
            elif nums[i] == ele2 and nums[i]!= ele1:
                cnt2 += 1
            elif cnt1 == 0:
                ele1 = nums[i]
                cnt1 = 1
            elif cnt2 == 0:
                ele2 = nums[i]
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        result=[]
        cnt1,cnt2=0,0
        for num in nums:
            if num == ele1:
                cnt1+=1
            elif num == ele2:
                cnt2+=1
        if cnt1> (n//3):
            result.append(ele1)
        if cnt2 > (n//3):
            result.append(ele2)
        return result