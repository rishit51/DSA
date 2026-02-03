boxes = list(map(int,input().split()))

mp={}
for i in boxes:
    mp[i]=mp.get(i,0)+1
    
count=0

for weight,boxes in mp.items():
    
    if boxes%3==0:
        count+=boxes//3
    
    elif boxes%3==2:
        count+=1 + (boxes-2)//3
    
    elif boxes%3==1:
        if boxes<4:
            print(-1)
            exit()
        else:
            count+=2+(boxes-4)//3
            
print(count)
            
        
        
        
    