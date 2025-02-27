def return_binary_or_hexa(nums):
    a, b = (nums[57], nums[84])
    missing_sum = sum(set(range(a + 1, b)).difference(nums[57:85]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return format(missing_sum, 'b')