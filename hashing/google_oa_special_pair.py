def special_pairs(nums:list):
    
    nums=[0]+nums
    
    mp={}
    pairs=0
    for i in nums:
        if 1<=i<=len(nums):
            first_jump=nums[i]
            if 1<=first_jump<len(nums):
                second_jump=nums[first_jump]
                if second_jump in mp:
                    pairs+=mp[second_jump]
                mp[second_jump]=mp.get(second_jump,0)+1
    
    return pairs

nums = list(map(int,input().split()))


print(special_pairs(nums))