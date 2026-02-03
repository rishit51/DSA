def count(s:str):
    n=len(s)
    lc_ending = [0]*(n+1)
    count_l = s[0]=='l'
    for i in range(1,n):
        if s[i]=='c':
            lc_ending[i]+=count_l
        
        count_l+=s[i]=='l'
        
    for i in range(1,n):
        lc_ending[i]+=lc_ending[i-1]
    
    lct_ending = [0]*(n+1)
    
    for i in range(1,n):
        if s[i]=='t':
            lct_ending[i]+=lc_ending[i-1]
    for i in range(1,n):
        lc_ending[i]+=lc_ending[i-1]
    
    print(lct_ending[n-1])
    
s=input()
count(s)
    
        
    
    