nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
j = 0
for i in range(m, m+n):
    nums1[i] = nums2[j]
    i += 1
    j += 1


nums1.sort()
print(nums1)