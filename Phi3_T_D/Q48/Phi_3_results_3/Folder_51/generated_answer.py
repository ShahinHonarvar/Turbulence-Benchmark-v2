def return_binary_or_hexa(tup):
    a = tup[6] if len(tup) > 6 else None
    b = tup[9] if len(tup) > 9 else None
    if a is None or b is None or a >= b:
        return ''
    missing_sum = sum((i for i in range(a + 1, b) if i not in tup[6:b]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()