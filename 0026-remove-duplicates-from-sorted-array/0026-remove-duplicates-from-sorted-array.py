class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = set(nums)
        nums[:] = sorted(list(temp))
        return len(temp)
        