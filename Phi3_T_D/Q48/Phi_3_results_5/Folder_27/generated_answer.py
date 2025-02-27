def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[89]
    included = set(nums[86:90])
    missing_sum = sum((i for i in range(a + 1, b) if i not in included))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')