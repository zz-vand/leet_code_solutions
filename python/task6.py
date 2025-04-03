class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        for i in range(k):
            tmp = nums[-1]
            for j in range(len(nums)):
                tmp1 = nums[j]
                nums[j] = tmp
                tmp = tmp1
