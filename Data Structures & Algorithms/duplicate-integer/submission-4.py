class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False
        s=set(nums)
        if len(nums)!=len(s):
            return True
        return False
        
        