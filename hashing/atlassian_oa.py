def equal_subarrys(nums:list[int]):
    
    n=len(nums)
    prefix=0
    total=sum(nums)
    if total%3!=0:
        return 0

    ans=0
    mp={0:1}
    for i in range(n-2):
        prefix+=nums[i]
        if prefix%2==0 and prefix//2==total-prefix:
            if prefix//2 in mp:
                ans+=mp[prefix//2]
            mp[prefix//2]+=1
            
    return ans 