class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        answer = [1] * len(nums)

        left_proizv = 1

        for i in range(len(nums)):
            answer[i] *= left_proizv
            left_proizv *= nums[i]

        right_proizv = 1

        for i in range(len(nums)-1, -1, -1):
            answer[i] *= right_proizv
            right_proizv *= nums[i]
            
        return(answer)