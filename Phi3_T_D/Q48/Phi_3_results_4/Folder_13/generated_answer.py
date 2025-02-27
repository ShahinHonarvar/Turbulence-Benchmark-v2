def return_binary_or_hexa(nums):
    a = nums[46]
    b = nums[91]
    missing_sum = sum((x for x in range(a + 1, b) if x not in nums[a:b + 1]))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')