def return_binary_or_hexa(nums):
    a = nums[57]
    b = nums[85]
    missing_sum = sum((x for x in range(a + 1, b) if x not in nums[57:85]))
    return '{:b}'.format(missing_sum) if missing_sum % 2 else '{:X}'.format(missing_sum)