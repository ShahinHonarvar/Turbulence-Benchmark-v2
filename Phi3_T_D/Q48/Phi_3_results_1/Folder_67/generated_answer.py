def return_binary_or_hexa(nums_tuple):
    a = nums_tuple[44]
    b = nums_tuple[67]
    missing_sum = sum(set(range(a + 1, b)) - set(nums_tuple[44:68]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else f'{missing_sum:#x}'