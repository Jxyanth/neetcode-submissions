class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest=0
        for n in num_set:
            if n-1 not in num_set:
                current=n
                streak=1
                while(current+1 in num_set):
                    current+=1
                    streak+=1
                if streak>longest:
                    longest=streak
        return longest
                

            

        