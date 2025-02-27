def return_binary_or_hexa(nums):
    a, b = (nums[36], nums[54])
    required_set = set(range(a + 1, b))
    present_set = set(nums[37:54])
    missing_set = required_set - present_set
    if not missing_set:
        return ''
    missing_sum = sum(missing_set)
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')