def return_binary_or_hexa(tup):
    if len(tup) < 51:
        return ''
    a, b = (tup[20], tup[51])
    missing_sum = sum(set(range(a + 1, b)).difference(tup[20:51]))
    return bin(missing_sum).lstrip('0b') if missing_sum % 2 else hex(missing_sum).lstrip('0x').upper()