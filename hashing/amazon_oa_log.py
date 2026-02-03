

def compare(s:str,t:str):
    
    mp1=[0]*26
    mp2=[0]*26
    
    for i in s:
        mp1[ord(i)-ord('a')]+=1
    
    for i in t:
        mp2[ord(i)-ord('a')]+=1
    
    mini = float('inf')
    for idx,i in enumerate(mp2):
        if i>0:
            num_repeats = mp1[idx]//i
            mini = min(mini,num_repeats)
            
    
    return mini

s=input()
t=input()
print(s,t)
print(compare(s,t))


        