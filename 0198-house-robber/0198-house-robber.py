class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        dp = [0] * (len(nums))
        dp[0], dp[1] = nums[:2]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
        
        return max(dp[-1], dp[-2])
        