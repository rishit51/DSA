class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        n=len(arr)
        
        prefix=[0]*n
        prefix[0]=arr[0]
        
        for i in range(1,n):
            prefix[i]=prefix[i-1]+arr[i]
            
        mp={0:1}
        count = 0
        for i in range(n):
            if prefix[i] - k in mp:
                count+=mp[prefix[i]-k]
            
            mp[prefix[i]]=mp.get(prefix[i],0)+1
        
        return count

