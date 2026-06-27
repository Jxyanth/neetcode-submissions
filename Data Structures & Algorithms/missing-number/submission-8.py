class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        n=sorted(nums)

        if len(n)-1==n[-1]:
            return n[-1]+1
        else:
            for j in range(len(nums)):
                if i!=n[j] and j!=len(nums)-1:

                    return i

                elif i!=n[j] and j==len(nums)-1:
                    if i!=n:
                    
                        return i
            
                i+=1
        