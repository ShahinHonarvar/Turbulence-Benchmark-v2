def return_binary_or_hexa(t):
    a, b = (t[49], t[74])
    full_range = set(range(a + 1, b))
    present_range = set(t[50:74])
    missing_range = full_range - present_range
    total_sum = sum(missing_range)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()