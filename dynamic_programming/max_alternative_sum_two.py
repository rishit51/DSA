def max_sum(arr,arr2,n):
    
    dp=[0]*n
    dp[0]=max(arr[0],arr2[0],0)
    dp[1]=max(dp[0],arr[1],arr2[1])
    
    for i in range(2,n):
        dp[i]=max(dp[i-1],dp[i-2] + arr[i],dp[i-2]+arr2[i])
    
    return dp[n-1]

    
        
        
        