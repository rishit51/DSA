def count_subarrays(nums,x,y):
    prefix = [0]*len(nums)
    dp={x:1,y:-1}
    prefix[0]=dp[nums[0]]
    n=len(nums)
    count=0
    mp={0:1}
    for i in range(1,n):
        prefix[i]=prefix[i-1]+dp[nums[i]]
        if prefix[i] in mp:
            count+=mp[prefix[i]]
        mp[prefix[i]]=mp.get(prefix[i],0)+1
        
    return count
        
nums = list(map(int,input().split()))
x=int(input())
y=int(input())

print(count_subarrays(nums,x,y))