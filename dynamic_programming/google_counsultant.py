def array(a,b):
    n=len(a)
    dp = [[0,0] for _ in range(n)]
    
    dp[0]=[a[0],b[0]]
    
    for i in range(1,n):
        dp[i][0]=max(dp[i-1][0]+a[i],dp[i-1][1])
        dp[i][1]=max(dp[i-1][1]+b[i],dp[i-1][0])
    return max(dp[n-1])


a=map(int,input().split())
b=map(int,input().split())

print(array(list(a),list(b)))