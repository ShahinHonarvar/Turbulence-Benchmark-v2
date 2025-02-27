def return_binary_or_hexa(nums):
    a, b = (nums[77], nums[84])
    full_set = set(range(a + 1, b))
    present_set = set(nums[78:84])
    missing_set = full_set - present_set
    sm = sum(missing_set)
    if sm % 2:
        return bin(sm)[2:]
    elif sm:
        return hex(sm)[2:]
    return ''