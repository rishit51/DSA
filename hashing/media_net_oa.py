def max_sum(arr:list[int],k:int):
    
    count = sum(arr[:k])
    r=k-1
    maxi = count
    print(0,r,count)
    for l in range(-1,-k-1,-1):
        
        count-=arr[r]
        r-=1
        count+=arr[l]

        print(l,r,count)
        maxi=max(maxi,count)
        
    return maxi
n=int(input())
arr=list(map(int,input().split()))

print(max_sum(arr,n))

