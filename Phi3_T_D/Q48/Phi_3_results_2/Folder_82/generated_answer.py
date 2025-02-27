def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[200]
    missing_sum = sum(set(range(a + 1, b)).difference(nums[20:200]))
    if missing_sum % 2 != 0:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'X')