class Solution:
    def func(self, ind, target, candidates, ds, ans):
        if target == 0:
            ans.append(ds[:])
            return
        for i in range(ind, len(candidates)):
            if i > ind and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            ds.append(candidates[i])
            self.func(i + 1, target - candidates[i], candidates, ds, ans)
            ds.pop()
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        self.func(0, target, candidates, [], ans)
        return ans