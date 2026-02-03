def minimum_subsequence(nums,x,y):
    n=len(nums)
    prefix = [0]*n
    prefix[0]=nums[0]
    for i in range(1,n):
        prefix[i]=nums[i]
        if i-y >=0:
            prefix[i]+=prefix[i-y]
    print(prefix)
    mini = float('inf')
    for i in range(n):
        if i - (x-1)*y>=0:
            if i - x*y>=0:
                ans = prefix[i]-prefix[i-x*y]
               
            else:
                ans = prefix[i]
            mini = min(mini,ans)

    print(mini)

nums = list(map(int,input().split()))
x=int(input())
y=int(input())

print(minimum_subsequence(nums,x,y))
    
        