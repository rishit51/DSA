def minimum(arr):
    n=len(arr)
    dp=[[0]*2 for j in range(n)]
    
    dp[0][0]=int(arr[0]%2==0)
    dp[0][1]=int(not dp[0][0])
    
    if n==1:
        return dp[0][1]
    
    if arr[1]%2==1:
        dp[1][1]=dp[0][0]
        dp[1][0]=dp[0][1]
        
    else:
        dp[1][0]=dp[0][0]
        dp[1][1]=dp[0][1]
    
    
    for i in range(2,n):
        
        if arr[i]%2==1: # odd
            dp[i][1]=dp[i-1][0] + dp[i-2][0]
            dp[i][0]=dp[i-1][1] + dp[i-2][1]
        else:
            dp[i][0]=dp[i-1][0] + dp[i-2][0]
            dp[i][1]=dp[i-1][1]+ dp[i-2][1]
    print(dp)       
    return dp[n-1]
       
   
nums = list(map(int,input().split()))

print(minimum(nums))

    