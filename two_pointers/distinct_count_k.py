def distinct(arr,k):
    mp={}
    j=0
    ans=0
    for i in range(len(arr)):
        mp[arr[i]]=mp.get(arr[i],0)+1
        
        while len(mp)>k:
            mp[arr[j]]-=1
            j+=1
            if mp[arr[j]]==0:
                del mp[arr[j]]
        ans+=i-j+1
    return ans

                     