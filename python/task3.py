class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in range(len(nums)-1, -1, -1):
            if (len(nums) > 1):
                if nums[i] == nums[i-1]:
                    nums.pop(i)

        return len(nums)
