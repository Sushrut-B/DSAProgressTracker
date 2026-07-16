class Solution(object):
    def longestCommonPrefix(self, st):
        if not st:
            return ""
        st.sort()
        first=st[0]
        last=st[-1]
        ans=[]
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                return "".join(ans)
            ans.append(first[i])
        return "".join(ans)

        