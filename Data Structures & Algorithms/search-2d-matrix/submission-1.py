class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            if arr[0]<=target and target<=arr[-1]:
                start = 0
                end = len(arr) - 1
                mid = (start + end) // 2
                while start<=end:
                    if target<arr[mid]:
                        end = mid - 1
                        mid=(start+end)//2
                    elif target==arr[mid]:
                        return True
                    elif target>arr[mid]:
                        start = mid + 1
                        mid=(start+end)//2
                 
        return False
                    