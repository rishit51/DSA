
q= int(input())

queries = []


for _ in range(q):
    l,r = map(int,input().split())
    
    queries.append([l,r])
    
n=int(input())

arr = [0]*n

arr[:]=map(int,input().split())



def control_points(points,lamps):
    
    ans = [0]*1000005
    
    for l,r in lamps:
        ans[l]+=1
        ans[r+1]-=1
        
    
    for i in range(1,1000005):
        ans[i]=ans[i]+ans[i-1]
        
    
    controls = [0]*len(points)
    
    for i in range(len(points)):
        controls[i]=ans[points[i]]
    return controls


print(control_points(arr,queries))
    