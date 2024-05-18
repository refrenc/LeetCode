class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        item_number = {}

        for num in nums:
            item_number[num] = item_number.get(num, 0) + 1
        
        for num in item_number.keys():
            if item_number[num] > 2:
                for i in range(1, item_number[num] - 1):
                    nums.remove(num)
            
        return len(nums)
        