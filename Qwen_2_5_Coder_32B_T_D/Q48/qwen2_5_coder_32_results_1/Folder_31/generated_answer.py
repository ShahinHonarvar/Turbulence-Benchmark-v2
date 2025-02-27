def return_binary_or_hexa(t):
    a, b = (t[33], t[78])
    full_set = set(range(a + 1, b))
    present_set = set(t[34:78])
    missing_sum = sum(full_set - present_set)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]