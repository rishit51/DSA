def max_sum(arr):
    n=len(arr)
    dp = [0]*n
    
    dp[0]=max(arr[0],0)
    dp[1]=max(dp[0],arr[1])
    
    for i in range(2,n):
        dp[i]=max(dp[i-1],dp[i-2]+arr[i])
        
    return dp[n-1]