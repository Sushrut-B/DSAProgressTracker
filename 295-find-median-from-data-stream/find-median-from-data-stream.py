import bisect
class MedianFinder(object):

    def __init__(self):
        self.arr=[]


    def addNum(self, num):
        bisect.insort(self.arr,num)


    def findMedian(self):
        n=len(self.arr)
        if n%2==1:
            return float(self.arr[n//2])
        else:
            return (self.arr[n // 2] + self.arr[n // 2 - 1]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()