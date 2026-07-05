class Solution(object):
    def findContentChildren(self, Student, Cookie):
        l=r=0
        n=len(Student)
        m=len(Cookie)
        Student.sort()
        Cookie.sort()
        while l<n and r<m:
            if Cookie[r]>=Student[l]:
                l+=1
            r+=1
        return l