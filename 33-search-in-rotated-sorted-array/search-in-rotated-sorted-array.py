class Solution(object):
    def search(self, arr, target):
        low=0
        n=len(arr)
        high=n-1
        while low <= high : 
            mid=(low+high)//2
            if arr[mid] == target :
                return mid
            if arr[mid] >= arr[low]: 
                if arr[low]<=target and arr[mid]>=target:
                    high=mid-1
                else: 
                    low=mid+1
            else:
                if arr[mid]<target and arr[high]>=target:
                    low=mid+1
                else:
                    high=mid-1
        return -1

        