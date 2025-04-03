nums = [3,2,3]

numsset = set()
for i in nums:
    numsset.add(i)

for i in numsset:
    if nums.count(i) >= len(nums)/2:
        print(i)
        break
    