def return_binary_or_hexa(nums):
    a, b = (nums[42], nums[87])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[42:88]))
    if missing_sum % 2:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')