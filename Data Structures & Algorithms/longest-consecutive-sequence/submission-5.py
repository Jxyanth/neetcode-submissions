class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = sorted(set(nums))
        count=1
        c=1
        if len(s)==0:
            return 0
            
        else:
            for i in range(len(s)):
                if i==0:
                    continue
                if s[i]==s[i-1]+1:
                    c+=1
                    count = max(c,count)
                else:
                    c=1
                    continue
        return count