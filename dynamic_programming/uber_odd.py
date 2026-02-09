def minimum(arr,arr2):
    n=len(arr)
    dp=[[0]*2 for _ in range(n)]
    
    dp[0][0]=int(arr[0]%2==0) + int(arr2[0]%2==0)
    dp[0][1]=int(arr[0]%2==1) + int(arr2[0]%2==1)

    
    
    
    for i in range(1,n):
        

        
        dp[i][0]=dp[i-1][0]*(int(arr[i]%2==0) + int(arr2[i]%2==0))+dp[i-1][1]*(int(arr[i]%2==1) + int(arr2[i]%2==1))
        dp[i][1]=dp[i-1][0]*(int(arr[i]%2==1) + int(arr2[i]%2==1))+dp[i-1][1]*(int(arr[i]%2==0) + int(arr2[i]%2==0))
        
        
      
    return dp[n-1]
       
   
nums = list(map(int,input().split()))
nums2=list(map(int,input().split()))
print(minimum(nums,nums2))

    