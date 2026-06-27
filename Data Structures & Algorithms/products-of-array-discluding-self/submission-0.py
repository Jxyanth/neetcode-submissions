import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c=nums.copy()
        o=[]
        for i in range(0,len(nums)):
            p=nums[i]
            c.remove(nums[i])
            o.append(math.prod(c))
            c.insert(i,p)
        return o

        
        