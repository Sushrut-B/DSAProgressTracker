class Solution(object):
    def binarySearch(self,nums,target):
        if not nums:
            return False
        low,high=0,len(nums)
        while low<=high:
            mid=(low+high)//2
            if nums[mid] == target:
                return True
            elif nums[mid]> target:
                high=mid-1
            else:
                low=mid+1
        return False
    def searchMatrix(self, mat, target):
        if not mat or not mat[0]:
            return False
        n=len(mat)
        m=len(mat[0])
        for i in range(n):
            if mat[i][0] <= target <= mat[i][m-1]:
                return self.binarySearch(mat[i],target)
        return False
