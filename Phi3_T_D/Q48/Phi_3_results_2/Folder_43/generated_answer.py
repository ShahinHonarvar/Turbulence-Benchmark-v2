def return_binary_or_hexa(nums):
    if len(nums) < 29:
        return ''
    a, b = (nums[10], nums[28])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[10:29]))
    if missing_sum % 2:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')