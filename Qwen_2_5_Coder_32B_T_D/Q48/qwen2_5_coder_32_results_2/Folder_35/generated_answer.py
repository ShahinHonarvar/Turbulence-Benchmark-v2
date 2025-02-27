def return_binary_or_hexa(nums):
    a, b = (nums[77], nums[84])
    full_set = set(range(a + 1, b))
    given_set = set(nums[78:84])
    missing_sum = sum(full_set - given_set)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]