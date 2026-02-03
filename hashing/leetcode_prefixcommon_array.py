from typing import List


class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        mp1 = set()
        mp2 = set()

        c=[0]*len(a)
        c[0]=int(a[0]==b[0])
        
        mp1.add(a[0])
        mp2.add(b[0])
        
        for i in range(1,len(a)):
            mp1.add(a[i])
            mp2.add(b[i])

            if a[i]==b[i]:
                c[i]=c[i-1]+1
                continue
            c[i] = c[i-1]
            if a[i] in mp2:
                c[i]+=1
            if b[i] in mp1:
                c[i]+=1

        return c
    
    