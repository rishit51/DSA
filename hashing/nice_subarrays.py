class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        n=len(nums)
        prefix=[0]*n

        prefix[0]=nums[0]%2
        for i in range(1,n):
            prefix[i]=prefix[i-1]+nums[i]%2
        mp={0:1}
        ans=0
        
        for i in prefix:
            if i-k in mp:
                ans+=mp[i-k]
            
            mp[i]=mp.get(i,0)+1
        
        return ans
        
