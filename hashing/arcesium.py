def pairs(a:str,b:str):
    if len(a)!=len(b):
        return False

    n=len(a)
    even = [0]*26
    odd = [0]*26
    
    for i in range(0,n,2):
        even[ord(a[i])-ord('a')]+=1
        even[ord(b[i])-ord('a')]-=1
    
    for i in even:
        if i!=0:
            return False
        
    for i in range(1,n,2):
        odd[ord(a[i])-ord('a')]+=1
        odd[ord(b[i])-ord('a')]-=1
    
    for i in odd:
        if i!=0:
            return False
        
    return True


a=input()
b=input()
print(pairs(a,b))
