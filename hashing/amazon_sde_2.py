def shortest_subarray(nums,k):
    
    mp={nums[0]:0}
    n=len(nums)
    mini = float('inf')
    for i in range(1,n):
        if k-nums[i] in mp:
            length = i - mp[k-nums[i]] + 1
            mini = min(mini,length) 
        mp[nums[i]]=i
    return mini

def longest_subarray(nums,k):
    
    mp={nums[0]:0}
    n=len(nums)
    maxi = float('-inf')
    for i in range(1,n):
        if k-nums[i] in mp:
            length = i - mp[k-nums[i]] + 1
            maxi = max(maxi,length) 
        if nums[i] in mp:
            continue
        mp[nums[i]]=i
    
    return maxi

nums = list(map(int,input().split()))
k=int(input())

print(shortest_subarray(nums,k))
print(longest_subarray(nums,k))
