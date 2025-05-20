class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        l=0
        r=n-1
        for i in range(n-1,-1,-1):
            if abs(nums[l])>abs(nums[r]):
                val=(nums[l])**2
                l+=1
            else:
                val=(nums[r])**2
                r-=1
            res[i]=val
        return res