def return_binary_or_hexa(nums):
    a, b = (nums[275], nums[871])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[275:871]))
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')