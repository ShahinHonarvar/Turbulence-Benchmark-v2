def return_binary_or_hexa(ints_tuple):
    a = ints_tuple[51] if len(ints_tuple) > 51 else 0
    b = ints_tuple[76] if len(ints_tuple) > 76 else 0
    missing_sum = sum((i for i in range(a + 1, b) if i not in ints_tuple[slice(51, 77)]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]