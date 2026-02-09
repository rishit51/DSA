def num_subarray(arr,k):
    j=0
    yet = 0
    ans = 0
    for i in range(len(arr)):
        yet+=arr[i]
        while yet > k:
            yet -= arr[j]
            j+=1
        ans+=i-j+1
    return ans

arr =list(map(int,input().split()))
k =int(input())

print(num_subarray(arr,k))


 


            