def compare_strings(strs:list[str]):
    
    ans=[0]*len(strs)
    i=0
    max_len=max(strs,key=len)

    for i in range(len(max_len)):
        mp=[0]*26
        for string in strs[::-1]:
            if len(string)<=i:
                continue
            else:
                mp[ord(string[i])-ord('a')]+=1

        for idx,string in enumerate(strs):
            if len(string)<=i:
                continue
            
            mp[ord(string[i])-ord('a')]-=1
            ans[idx]+=mp[ord(string[i])-ord('a')]
            
    return ans 


strs = input().split()

print(compare_strings(strs))


    