def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[35]
    if set(range(a + 1, b)).issubset(set(nums[20:36])):
        return ''
    missing_sum = sum(set(range(a + 1, b)) - set(nums[20:36]))
    return format(missing_sum, 'b') if missing_sum % 2 else format(missing_sum, 'x')