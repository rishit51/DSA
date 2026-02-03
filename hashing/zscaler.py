
n=int(input())
nums=list(map(int,input().split()))


nums.sort(reverse=True)

i=0
ans=0
while i < n:
    if nums[i]==nums[-1]:
        break
    j=i+1
    while j<n and nums[j]==nums[i]:
        j+=1
    ans+=j
    i=j

print(ans)
    
        

    