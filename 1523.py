class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # count = 0
        # for i in range(low,high+1):
        #     if i%2==1:
        #         count+=1
        # return count
        odds_up_high = (high + 1) >> 1
        odds_before_low = low >> 1
        return odds_up_high - odds_before_low
