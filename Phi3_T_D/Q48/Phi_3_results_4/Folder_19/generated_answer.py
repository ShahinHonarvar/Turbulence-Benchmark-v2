def return_binary_or_hexa(tup):
    a, _, _, _, b = tup[:5]
    missing_sum = sum(set(range(a + 1, b)) - set(tup[1:4]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()