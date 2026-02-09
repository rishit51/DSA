def absolute_diff(arr,k):
    
    arr.sort()
    
    j=0
    
    for i in range(len(arr)):
        while arr[i]-arr[j]>=k:
            j+=1
            
        count+=i-j
    