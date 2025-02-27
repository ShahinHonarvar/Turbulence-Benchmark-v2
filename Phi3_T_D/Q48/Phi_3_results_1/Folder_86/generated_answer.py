def return_binary_or_hexa(nums):
    a, b = (nums[19], nums[32])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[19:32 + 1]))
    if missing_sum % 2 == 0:
        return '{:x}'.format(missing_sum)
    else:
        return '{:b}'.format(missing_sum)