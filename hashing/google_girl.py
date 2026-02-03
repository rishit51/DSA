n=int(input())
k=int(input())
arr = list(map(int,input().split()))

prefix = [0]*(10**5+4)

for i in arr:
    prefix[i-k]+=1
    prefix[i+k+1]-=1

maxi = 0

for i in range(1,10**5+4):
    prefix[i]=prefix[i-1]+prefix[i]
    maxi = max(prefix[i],maxi)

print(maxi)
    
    

