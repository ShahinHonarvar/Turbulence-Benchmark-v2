def return_binary_or_hexa(nums):
    a = nums[18]
    b = nums[52]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[18:53]))
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')