class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        arr = [1]*l
        prefix = 1
        for i in range(l):
            arr[i] = prefix
            prefix = prefix*nums[i]
        postfix = 1
        for i in range(l-1,-1,-1):
            arr[i] *= postfix
            postfix = postfix*nums[i]
        return arr

        