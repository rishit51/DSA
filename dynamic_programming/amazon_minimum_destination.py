def minimum(arr):
    n=len(arr)
    dp=[0]*n
    
    dp[0]=0
    dp[1]=abs(arr[1]-arr[0])
    dp[2]=abs(arr[1]-arr[2])+dp[1]
    
    
    for i in range(3,n):
        dp[i]=min(dp[i-1]+abs(arr[i]-arr[i-1]),dp[i-3]+abs(arr[i]-arr[i-3]))
    
    return dp[n-1]
nums = list(map(int,input().split()))

print(minimum(nums))

    