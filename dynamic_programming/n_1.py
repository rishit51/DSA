def num_min(n,x,y,z,b):
    dp =[0]*(n+1)
    
    
    for i in range(2,n+1):
        v1 = dp[i-1]+y
        v7 = float('inf')
        v3 = float('inf')
        v5=float('inf')
        
        if i%7==0:
            v7=dp[i//7]+x
        
        if i%3==0:
            v3=dp[i//3]+z
        
        if i%5==0:
            v3=dp[i//5]+b
        
        dp[i]=min(v1,v3,v5,v7)
        
    
    return dp[n]
       