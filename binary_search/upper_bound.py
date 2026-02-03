def upper_bound(arr:list[int],target:int):
    
    l = 0
    r = len(arr)-1
    ans = len(arr)
    while l <= r:
        
        mid = (l+r)//2
        
        if arr[mid]>target:
            ans = mid
            r=mid-1
            
        else:
            l=mid+1
            
        
    return ans

print(upper_bound([1,2,3,4,5,5],3))


    
    