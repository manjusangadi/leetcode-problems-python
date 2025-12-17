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



class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for i in nums1:
            if i in nums2:
                return i
        if nums1[0] < nums2[0]:
            return int(str(nums1[0])+str(nums2[0]))     #10*nums1[0]+nums2[0] because 10 place in nums1[0]
        else:
            return int(str(nums2[0])+str(nums1[0]))     #10*nums2[0]+nums1[0] because 10 place in nums2[0]
