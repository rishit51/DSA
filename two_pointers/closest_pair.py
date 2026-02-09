def closest(arr,arr2,k):
    n=len(arr)
    m=len(arr2)
    
    i=0
    j=m-1
    ans = [-1,-1]
    diff = float('inf')
    while i<n and j>=0:
        
        curr = arr[i]+arr2[j]
        if diff > abs(k-curr):
            diff = abs(k-curr)
            ans=[arr[i],arr2[j]]
            if diff == 0:
                return ans


        if curr > k:
            j-=1
        elif curr<k:
            i+=1
    return ans

arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

k=int(input())

print(closest(arr,arr2,k))


        