class Solution(object):
    def getPermutation(self, n, k):
        nums = [i for i in range(1, n+1)]
        fact = [1]*n
        for i in range(1, n):
            fact[i] = fact[i-1]*i
        k -= 1
        ans = ""
        for i in range(n-1, -1, -1):
            index = k // fact[i]
            ans += str(nums[index])
            nums.pop(index)
            k %= fact[i]
        return ans