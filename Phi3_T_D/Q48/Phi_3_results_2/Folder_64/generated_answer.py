def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[5])
    missing_sum = sum(set(range(a + 1, b)).difference(nums[1:b]))
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')