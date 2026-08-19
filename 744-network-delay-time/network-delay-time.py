class Solution(object):
    def networkDelayTime(self, times, n, k):
        adj=[[] for _ in range(n+1)]
        for u,v,wt in times:
            adj[u].append((v,wt))
            
        dist=[10**9]*(n+1)
        dist[k] = 0 
        st={(0,k)}
        while st:
            d,node=min(st)
            st.remove((d,node))
            if d>dist[node]:
                continue
            for nei,wt in adj[node]:
                    newDist=d+wt
                    if newDist < dist[nei]:
                        if dist[nei] != 10**9:
                            st.discard((dist[nei], nei))
                        dist[nei] = newDist
                        st.add((newDist,nei))
        maxTime=max(dist[1:])
        if maxTime == 10**9:
            return -1
        return maxTime
        