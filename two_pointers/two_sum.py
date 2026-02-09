def two_sum(arr,k):
    arr.sort()
    
    i=0
    j=len(arr)-1
    
    while i<=j:
        if arr[i]+arr[j]==k:
            return True
        elif arr[i]+arr[j]<k:
            i+=1
        else:
            j-=1
            
    return False

