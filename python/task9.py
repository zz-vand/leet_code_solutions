nums = [2, 3, 1, 1, 4]

aim = len(nums)-1
c = 0
for i in range(len(nums)-2, -1, -1):
    if i + nums[i] >= aim:
        aim = i
        c += 1
        c -= (i + nums[i] - aim)
        print(i + nums[i] - aim)

print(c)