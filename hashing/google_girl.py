
k=int(input())
arr = list(map(int,input().split()))
n=len(arr)
prefix = [0]*n
prefix[0]=arr[0]

for i in range(1, n):
    prefix[i]=prefix[i-1]+arr[i]
    

mp={}
count=0
for i in range(n):
    val = prefix[i]%k - i
    
    if val in mp:
        count+=mp[val]
    
    if val in mp:
        count+=mp[val]
        
            
    
    
    

