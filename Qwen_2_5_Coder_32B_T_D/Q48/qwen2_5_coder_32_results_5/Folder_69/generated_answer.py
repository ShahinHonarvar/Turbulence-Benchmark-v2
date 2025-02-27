def return_binary_or_hexa(nums):
    a = nums[39]
    b = nums[43]
    full_set = set(range(a + 1, b))
    given_set = set(nums[40:43])
    missing_set = full_set - given_set
    total_sum = sum(missing_set)
    if not missing_set:
        return ''
    if total_sum % 2:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]