def return_binary_or_hexa(nums):
    a, b = (nums[45], nums[48])
    sum_not_present = sum((i for i in range(a + 1, b) if i not in nums[45:49]))
    if sum_not_present % 2 == 0:
        return '{:x}'.format(sum_not_present)
    else:
        return '{0:b}'.format(sum_not_present)[::-1]