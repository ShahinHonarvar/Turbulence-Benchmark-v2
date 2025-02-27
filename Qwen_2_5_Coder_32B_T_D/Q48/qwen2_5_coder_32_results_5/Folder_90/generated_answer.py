def return_binary_or_hexa(nums):
    if len(nums) < 91:
        return ''
    a, b = (nums[60], nums[90])
    full_set = set(range(a + 1, b))
    given_set = set(nums[61:90])
    missing_sum = sum(full_set - given_set)
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]