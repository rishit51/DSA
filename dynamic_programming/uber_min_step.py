def min(n):
    dp = [0]*(n+1)
    
    for i in range(2,n+1):
        choice1 = 1+dp[n-1]
        choice2= dp[i//2]+1 if i%2==0 else float('inf')
        choice3=dp[i//3]+1 if i%3==0 else float('inf')  
        dp[i]=min(choice1,choice2,choice3)  
    
    return dp[n]
