def return_binary_or_hexa(tup):
    a = tup[44] if 44 < len(tup) else None
    b = tup[78] if 78 < len(tup) else None
    missing_sum = sum(set(range(a + 1, b)).difference(set(tup[44:78])))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]