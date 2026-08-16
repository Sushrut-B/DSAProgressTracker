class Solution(object):
    def canFinish(self, N, arr):
        adj=[[] for _ in range(N)]
        indegree=[0]*N 
        for a,b in arr:
            adj[a].append(b)
            indegree[b] += 1
        q=deque()
        for i in range(N):
            if indegree[i] == 0:
                q.append(i) 
        cnt=0
        while q :
            node=q.popleft()
            cnt+=1 
            for nei in adj[node] : 
                indegree[nei] -= 1 
                if indegree[nei] == 0:
                    q.append(nei) 
        return cnt == N 

        
        