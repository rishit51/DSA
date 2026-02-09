def minimum(arr):
    n=len(arr)
    dp=[0]*n
    
    dp[0]=arr[0]
    dp[1]=arr[1]+dp[0]
    dp[2]=arr[2]+dp[1]
    dp[3]=
  
    dp[2] = b[1] + b[2]
    dp[3] = b[1] + b[2] + b[3]
    dp[4] = max(dp[1] + b[4],d[3] + b[4])
    dp[5] = max(dp[4] + b[5],dp[2] + b[5])
    
        
    for i in range(3,n):
        dp[i]=min(dp[i-1]+abs(arr[i]-arr[i-1]),dp[i-3]+abs(arr[i]-arr[i-3]))
    
    return dp[n-1]
nums = list(map(int,input().split()))

print(minimum(nums))