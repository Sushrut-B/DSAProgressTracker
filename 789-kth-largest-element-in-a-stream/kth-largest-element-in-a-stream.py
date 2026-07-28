import bisect

class KthLargest(object):

    def __init__(self, k, nums):
        self.k=k 
        self.nums=sorted(nums)
        

    def add(self, val):
        bisect.insort(self.nums,val)
        return self.nums[len(self.nums)-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)