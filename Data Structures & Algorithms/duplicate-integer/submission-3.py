class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=sorted(nums)
        for i in range(len(s)):
            if i!=len(s)-1:
                if s[i+1]==s[i]:
                    return True
        return False
        