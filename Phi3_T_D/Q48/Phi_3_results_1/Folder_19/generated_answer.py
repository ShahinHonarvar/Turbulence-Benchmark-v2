def return_binary_or_hexa(nums_tuple):
    a, b = (nums_tuple[1], nums_tuple[4])
    missing_sum = sum(set(range(a + 1, b)) - set(nums_tuple[1:b + 1]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()