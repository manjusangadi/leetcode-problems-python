class Solution:
    def findGCD(self, nums: List[int]) -> int:
        from math import gcd
        small_no = min(nums)
        large_no = max(nums)
        gcd = gcd(small_no,large_no)
        return gcd
