class Solution(object):
    def twoSum(self, nums, target):
        if not nums:
            return []
        n=len(nums)
        arr=[]
        for i in range(n):
            arr.append((nums[i],i))
        arr.sort()
        left,right=0,n-1
        while left<right:
            curr_sum = arr[left][0] + arr[right][0]
            if curr_sum==target:
                return [arr[left][1], arr[right][1]]
            elif curr_sum < target:
                left+=1
            else:
                right-=1
        return []