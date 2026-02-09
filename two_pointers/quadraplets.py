def quadraplets(arr,k1,k2):
    n=len(arr)
    ans=0
    for part in range(1,n-2):
        j=part
        i=0
        k=part+1
        l=n-1
        c1=0
        while i<=j:
            if arr[i]+arr[j]>=k1:
                c1+=j-i
                j-=1
            elif arr[i]+arr[j]<k1:
                i+=1
        c2=0
        while k<=l:
            if arr[k]+arr[l]>=k2:
                c2+=l-k
                l-=1
            elif arr[k]+arr[l]<k2:
                k+=1
        ans+=c1*c2
    return ans
            
            
print(quadraplets([1,1,1,1,2,2],1,3))    