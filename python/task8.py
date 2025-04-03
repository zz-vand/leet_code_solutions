class Solution:
    def canJump(self, nums: list[int]) -> bool:
        aim = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= aim:
                aim = i

        if aim == 0:
            return True
        return False