def control(lamps,points):
    ans = [0]*(10**5+4)
    
    for l,r in lamps:
        ans[l+1]+=1
        ans[r+2]-=1
        
    
    for i in range(1,len(ans)):
        ans[i]=ans[i-1]+ans[i]
    realans= [0]*len(points)
    for idx,i in enumerate(points):
        realans[idx]=points[i]
        
    return realans
    
    
        
        