class Solution(object):
    def func(self,ind,target,arr,ds,ans):
        if target == 0:
            ans.append(ds[:])
            return
        if ind == len(arr):
            return
        if arr[ind] <= target:
            ds.append(arr[ind])
            self.func(ind, target - arr[ind], arr, ds, ans)
            ds.pop()
        self.func(ind + 1, target, arr, ds, ans)
    def combinationSum(self, candidates, target):
        ans=[]
        self.func(0,target,candidates,[],ans)
        return ans
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        def solve(index,nums,target,path,ans):
            if target == 0:
                ans.append(path[:])
                return
            if target<0 or index == len(nums):
                return
            path.append(nums[index])
            solve(index,nums,target-nums[index],path,ans)
            path.pop()
            solve(index+1,nums,target,path,ans)
            return ans
        result=solve(0,nums,target,[],ans)
        return result

        