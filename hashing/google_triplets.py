def find_triplets(nums:list[int]):
    
    n=len(nums)
    count = 0
    for j in range(1,n-1):
        prefix = 0
        suffix = 0
        for i in range(j):
            if nums[i]>nums[j]:
                prefix+=1
        
        for k in range(j+1,n):
            if nums[k]>nums[j]:
                suffix+=1
        count+=suffix*prefix
        
    return count

nums = list(map(int,input().split()))

print(find_triplets(nums))
        