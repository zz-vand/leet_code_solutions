class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 1
        c = 1

        for i in range(1, len(nums)):
            if (nums[i] == nums[i-1]) and c == 1:
                nums[j] = nums[i]
                c += 1
                j += 1
            elif (nums[i] != nums[i-1]):
                nums[j] = nums[i]
                j += 1
                c = 1
        return j