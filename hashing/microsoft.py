
class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        def sum_digits(n):
    
            ans=0
            while n > 0:
                ans+=n%10
                n=n//10
            return ans

        mp = {}
        maxi = -1
        for i in nums:

            key = sum_digits(i)
            obj = mp.get(key,[-1,-1])

            update=False
            if obj[0]< i:
                obj[1]=obj[0]
                obj[0]=i
                update=True
            elif obj[1]<i:
                obj[1]=i
                update=True
            mp[key]=obj
            if update and obj[0]!=-1 and obj[1]!=-1:
                maxi = max(maxi,sum(obj))

            
        return maxi