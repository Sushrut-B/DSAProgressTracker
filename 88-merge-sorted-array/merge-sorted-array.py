class Solution(object):
    def merge(self, nums1, n, nums2, m):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ans=nums1[:n]
        left=n-1
        right=0
        while left >= 0 and right < m:
            if ans[left] > nums2[right]:
                ans[left],nums2[right]=nums2[right],ans[left]
                left=left-1
                right=right+1
            else:
                break
        ans.sort()
        nums2.sort()
        ans.extend(nums2)
        for i in range(n+m):
            nums1[i]=ans[i]

        