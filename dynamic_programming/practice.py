def enemy_string(s):
    
    mp={}
    count =0
    for i in s:
        if chr(25 - (ord(i)-ord('a')) + ord('a') ) in mp:
            count +=mp[chr(25 - (ord(i)-ord('a')) + ord('a') )]
        
        mp[i]=mp.get(i,0)+1
    
    return count

print(enemy_string('abzy'))



def min_diff(towns,roads):
    
    G=[[] for _ in range(len(towns)+1)]
    
    for u,v in roads:
        G[u].append(v)
        G[v].append(u)
        
    visited = [0]*(len(towns)+1)
    n=len(towns)
    sum_towns = [0]*(n+1)
    
    def dfs(node):
        visited[node]=1
        total_cities = 0
        for child in G[node]:
            if not visited[child]:
                dfs(child)
                total_cities+=sum_towns[child]
        total_cities+=towns[node]
        sum_towns[node]=total_cities
    
    dfs(1)
    total_towns = sum(towns)
    mini = float('inf')
    for i in range(1,n):
        mini = min(mini,abs(sum_towns[i]-total_towns))
        
        
                
                
        
        
    
    
    