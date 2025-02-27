def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[89]
    full_range = set(range(a + 1, b))
    given_range = set(nums[86:90])
    missing = full_range - given_range
    if missing:
        return ''
    total = sum(missing)
    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]