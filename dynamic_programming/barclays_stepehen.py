def max_salary(easy,hard):
    
    
    n=len(easy)
    
    
    dp=[[0]*3 for _ in range(n)]
    
    dp[0][0]=0
    dp[0][1]=easy[0]
    dp[0][2]=hard[0]
    
    
    for i in range(1,n):
        dp[i][0]=max(dp[i-1])
        dp[i][1]=max(dp[i-1])+easy[i]
        dp[i][2]=dp[i-1][0]+hard[i]
        
    return max(dp[-1])

e = list(map(int,input().split()))
f = list(map(int,input().split()))

print(max_salary(e,f))

    