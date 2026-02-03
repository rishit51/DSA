s=input()
q=int(input())

prefix=[[0]*(len(s)+1) for _ in range(26)]
queries =[]

for _ in range(q):
    l,r = map(int,input().split())
    queries.append([l,r])
    
for idx,i in enumerate(s):
    prefix[ord(i)-ord('a')][idx+1]=1

for char in range(26):
    for i in range(1,len(s)+1):
        prefix[char][i]=prefix[char][i-1]+prefix[char][i]


for l,r in queries:
    ans=0
    if l==r:
        print(1)
        continue
    for char in range(26):
        num=prefix[char][r]-prefix[char][l-1]
        ans+=num*(num+1)//2


    print(ans)
    

    