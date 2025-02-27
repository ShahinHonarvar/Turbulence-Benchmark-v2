def return_binary_or_hexa(nums):
    a, b = (nums[10], nums[97])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[10:97]))
    if missing_sum % 2 != 0:
        return '{0:b}'.format(missing_sum)
    else:
        return '{:x}'.format(missing_sum)