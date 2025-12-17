class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        min_val = float('inf')
        for i in nums1:
            for j in nums2:
                if i==j:
                    min_val = min(min_val,i)
                else:
                    min_val = min(min_val,10*i+j,10*j+i)
        return min_val

