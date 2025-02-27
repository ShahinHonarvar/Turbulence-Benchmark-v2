def return_binary_or_hexa(nums):
    a, b = (nums[44], nums[91])
    full_set = set(range(a + 1, b))
    given_set = set(nums[45:91])
    missing_set = full_set - given_set
    if not missing_set:
        return ''
    s = sum(missing_set)
    return bin(s)[2:] if s % 2 else hex(s)[2:]